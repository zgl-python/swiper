from django.shortcuts import render
from user import logics
from common import errors
from common import keys
from libs.http import render_json
from django.core.cache import cache
from user.models import User
 
# Create your views here.

def get_vcode(request):
    """获取验证码"""
    phonenum = request.POST.get('phonenum')
    print(phonenum)
    # 检查手机号是否合法
    if logics.is_phonenum(phonenum):
        # 发送验证码
        logics.send_vcode(phonenum)
        return render_json()
    else:

        return render_json(code=errors.PHONENUM_ERR)


def check_vcode(request):
    """检查验证码"""
    phonenum = request.POST.get('phonenum')
    vcode  = request.POST.get('vcode')

    # 检查手机号是否合法
    if logics.is_phonenum(phonenum):
        cached_vcode = cache.get(keys.VCODE_KEY % phonenum)  # 从缓存获取验证码
        if cached_vcode == vcode:
            try:
                user = User.objects.get(phonenum=phonenum)
            except User.DoesNotExist:
                # 如果账号不存在，直接创建出来
                user = User.objects.create(phonenum=phonenum, nickname=phonenum)
            
            # 在session中记录登录状态
            request.session['uid'] = user.id
            return render_json(data=user.to_dict())
        else:
            return render_json(code=errors.VCODE_ERR)
    else:
        return render_json(code=errors.PHONENUM_ERR)
    

def get_profile(request):
    '''获取个人资料'''
    profile_data = request.user.profile.to_dict()
<<<<<<< Updated upstream
    return render_json(profile_data)
=======
    return render_json(profile_data)

def set_profile(request):
    '''设置个人资料'''
    form = ProfileForm(request.POST)
    if form.is_valid():
        profile = form.save(commit=False)    # 只创建了一个profile对象并不提交
        profile.id = request.session['uid']  # 将用户与profile进行绑定
        profile.save()
        return render_json()
    else:
        return render_json(data=form.errors, code=errors.PROFILE_ERR)
    

def upload_avatar(request):
    """上传头像"""
    avatar = request.FILES.get('avatar')
    print(avatar, type(avatar))
    filename, full_path = logics.save_upload_file(request.user.id, avatar)
    request.user.avatar = full_path
    request.user.save()
    return render_json(code='ok')
>>>>>>> Stashed changes
