# -*- cording：utf-8 -*-
import json
import allure
import pytest
import requests
from Webapi import keys
from ddt.params import workflow  #拿取用例数据
class Test_Yuanting:
    def setup_class(self):
        print('开始')
    def teardown_class(self):
        print('结束')
    @allure.story('原霆后台')
    @pytest.mark.parametrize('listcases', workflow()['workflow'])
    def test_comm(self,listcases):
        #print('listcases内容')
        #print(listcases)
        #print('listcases类型'+type(listcases))
        allure.dynamic.title(listcases['title'])
        allure.dynamic.description(listcases['description'])
        testcases = listcases['cases']
        #print(testcases)
        for cases in testcases:
            listcase = list(cases.values())
            #print(listcase)
            url=listcase[3]
            datas=listcase[2]
            with allure.step(listcase[0]):
                ree=keys.post(url,datas)
                #assert ree.json()['code'] == 0
                #ree=ree.text
                #allure.attach(body=ree,name='返回参数',attachment_type=allure.attachment_type.TEXT)
                #print(ree)




    # def test_login(self):
    #     self.data=requests.post('https://cdc.test.yuanting.cn/api/passport/login',data={'account':"ycc000",'password':"1111"})
    #     self.datas=self.data.json()
    #     self.datas=self.datas['data']['token']
    #     return self.datas
    # def test_start(self):
    #     self.header=keys.login()
    #     self.data=requests.post('https://cdc.test.yuanting.cn/api/oa/process/start',data={"name":"[202301172144] ycc000[ycc000]的出差申请","processDefinitionKey":"trip_2000"},headers={"authorization":self.header})
    #     self.datas=self.data.text
    #     print(self.datas)

    # def test_login(self):
    #     self.ree=keys.post('https://cdc.test.yuanting.cn/api/passport/login',data={'account':"ycc000",'password':"1111"})
    #     self.datas=self.data.json()
    #     self.datas=self.datas['data']['token']
    #     return self.datas
    # def test_start(self):
    #     self.header = keys.login()
    #     url='oa/process/start'
    #     data={"name":"ycc000的出差申请","processDefinitionKey":"trip_2000"}
    #     self.ree=keys.post_test(url,data)
    #     self.ree=self.ree.json()
    #     self.da=self.ree['data']['processInstanceId']
    #     print(self.da)
    #     self.data = requests.post('https://cdc.test.yuanting.cn/api/oa/process/complete',
    #                               data={"taskId": "87741", "processInstanceId": self.da, "application": "y",
    #                                     "startTime": 1674116074000, "endTime": 1674288874000,
    #                                     "leaveType": {"id": "144434548803895296", "name": "流调"},
    #                                     "leaveDuration": "2.0", "address": "资中", "isOut": {"id": "1", "name": "是"},
    #                                     "reason": "213", "fujian": [{
    #                                                                     "id": "https://doc.yuanting.cn/model/file/202301/0d844adacffe970c50638d4b2eb379f118161632.png",
    #                                                                     "url": "https://doc.yuanting.cn/model/file/202301/0d844adacffe970c50638d4b2eb379f118161632.png",
    #                                                                     "name": "0d844adacffe970c50638d4b2eb379f1.png_wh860.png",
    #                                                                     "uid": 1674029792677, "status": "success"}]},headers={"authorization":self.header})
    #     self.datas = self.data.json()
    #     print(self.datas)

    # def test_start(self):
    #     self.header=keys.login()
    #     self.data=requests.post('https://cdc.test.yuanting.cn/api/oa/process/complete',data={"taskId":"87741","processInstanceId":"88232","application":"y","startTime":1674116074000,"endTime":1674288874000,"leaveType":{"id":"144434548803895296","name":"流调"},"leaveDuration":"2.0","address":"资中","isOut":{"id":"1","name":"是"},"reason":"213","fujian":[{"id":"https://doc.yuanting.cn/model/file/202301/0d844adacffe970c50638d4b2eb379f118161632.png","url":"https://doc.yuanting.cn/model/file/202301/0d844adacffe970c50638d4b2eb379f118161632.png","name":"0d844adacffe970c50638d4b2eb379f1.png_wh860.png","uid":1674029792677,"status":"success"}]},headers={"authorization":self.header})
    #     self.datas=self.data.text
    #     print(self.datas)