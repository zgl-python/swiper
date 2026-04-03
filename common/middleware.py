from django.utils.deprecation import MiddlewareMixin

from libs.http import render_json
from common import errors
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    AUTH_URL_WHITE = [
        'api/user/get_vcode',
        'api/user/check_vcode'
    ]

    def process_request(self, request):
        # 检查当前的url是否在白名单内
        if request.path in self.AUTH_URL_WHITE:
            # 白名单内的url直接跳出
            return
        # 检查用户是否登录
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
                return
            except User.DoesNotExist:
                return render_json(code=errors.USER_NOT_EXIST)
            
        else:
            return render_json(code=errors.LOGIN_REQIRED)