import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20210111 import sms_client, models
from flask import Response, Flask
from flask import request
app = Flask(__name__)
@app.route('/smssend',methods=['POST','GET'])
def send():
    value = request.args.get('phone')
    number = value.split()
    list1 = len(number)
    for i in range(list1):
        try:
            # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥>对的保密
            # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
            cred = credential.Credential("user", "password")
            # 实例化一个http选项，可选的，没有特殊需求可以跳过
            httpProfile = HttpProfile()
            httpProfile.endpoint = "sms.tencentcloudapi.com"
            # 实例化一个client选项，可选的，没有特殊需求可以跳过
            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            # 实例化要请求产品的client对象,clientProfile是可选的
            client = sms_client.SmsClient(cred, "ap-nanjing", clientProfile)
            # 实例化一个请求对象,每个接口都会对应一个request对象
            req = models.SendSmsRequest()
            params = {
                    "PhoneNumberSet": number,
                    "SmsSdkAppId": "1400710575",
                    "TemplateId": "1483200",
                    "SignName": "IT开源分享"
            }
            req.from_json_string(json.dumps(params))
            # 返回的resp是一个SendSmsResponse的实例，与请求对象对应
            resp = client.SendSms(req)
            # 输出json格式的字符串回包
            print (resp.to_json_string())
            return (resp.to_json_string())
        except TencentCloudSDKException  as err:
            return (str(err))
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1234,debug=True)
