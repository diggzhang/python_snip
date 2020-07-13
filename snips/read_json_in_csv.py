import pandas as pd
import json

get_left = pd.read_csv("/Users/xingze/Downloads/onion-event_event_20200713_155159.csv", header=None)
get_right = pd.read_csv("/Users/xingze/Downloads/onion-event_test-onion_20200713_155207.csv", header=None)

left_list = get_left[0].tolist()
right_list = get_right[0].tolist()

left_ready_diff = []
for elem in left_list:
    left_ready_diff.append(
        json.loads(elem)['uuid']
    )

right_ready_diff = []
for elem in right_list:
    right_ready_diff.append(
        json.loads(elem)['uuid']
    )

print(
    set(left_ready_diff) - set(right_ready_diff)
)
print(
    set(right_ready_diff) - set(left_ready_diff)
)




# """
# onion-event_test-onion中独有的
# {'9a9329f3-02b8-4f8f-8774-aee520e5ac89', 'bbb59373-c378-43eb-9e60-74381d023847', 'c940ce17-1d3b-478c-a8f7-a7b15d1a788a', 'a0f2aae2-1540-499f-8098-d2ae48ad292e', '1c6a506e-088a-4382-bbd2-a8a6f58aa3f7', '062a27f7-da44-4808-af79-26e95e2f2c85', 'b439ad0d-c26f-4684-baf1-b7b2f0db94da'}
#  "{""device"": ""bb9ff1cba21c6572"", ""imei"": ""861202045788445"", ""platform"":      ""app"", ""os"": ""android"", ""u_channel"": ""huawei"", ""productId"": ""02"",       ""netConfig"": ""wifi"", ""session"": ""a91983b8-8cba-4cb1-87ff-86227391ae37"",       ""d_app_version"": ""1.18.1"", ""d_model_brand"": ""TAS-AL00"", ""d_model_name"":     ""HUAWEI"", ""d_os_version"": ""10"", ""u_user"": ""5dd495f95178050f58327c07"",       ""u_role"": ""teacher"", ""u_VIP"": ""vip#3-1"", ""u_lastStageId"": 3,                ""u_lastSubjectId"": 1, ""u_text_edition"": ""1"", ""u_lastSemesterId"": 22,          ""category"": ""HomePage"", ""eventKey"": ""enterHomePageTest"", ""eventTime"":       1594526408927, ""uuid"": ""a0f2aae2-1540-499f-8098-d2ae48ad292e"", ""type"": ""C"",   ""serverTime"": 1594526410000, ""ip"": ""106.112.84.240""}",,,,
#  "{""device"": ""bb9ff1cba21c6572"", ""imei"": ""861202045788445"", ""platform"":      ""app"", ""os"": ""android"", ""u_channel"": ""huawei"", ""productId"": ""02"",       ""netConfig"": ""wifi"", ""session"": ""a91983b8-8cba-4cb1-87ff-86227391ae37"",       ""d_app_version"": ""1.18.1"", ""d_model_brand"": ""TAS-AL00"", ""d_model_name"":     ""HUAWEI"", ""d_os_version"": ""10"", ""u_user"": ""5dd495f95178050f58327c07"",       ""u_role"": ""teacher"", ""u_VIP"": ""vip#3-1"", ""u_lastStageId"": 3,                ""u_lastSubjectId"": 1, ""u_text_edition"": ""1"", ""u_lastSemesterId"": 22,          ""category"": ""HomePage"", ""eventKey"": ""enterPublisherCatalogPage"",              ""eventTime"": 1594526410051, ""uuid"": ""bbb59373-c378-43eb-9e60-74381d023847"",     ""serverTime"": 1594526410000, ""ip"": ""106.112.84.240""}",,,,
#  "{""device"": ""bb9ff1cba21c6572"", ""imei"": ""861202045788445"", ""platform"":      ""app"", ""os"": ""android"", ""u_channel"": ""huawei"", ""productId"": ""02"",       ""netConfig"": ""wifi"", ""session"": ""a91983b8-8cba-4cb1-87ff-86227391ae37"",       ""d_app_version"": ""1.18.1"", ""d_model_brand"": ""TAS-AL00"", ""d_model_name"":     ""HUAWEI"", ""d_os_version"": ""10"", ""u_user"": ""5dd495f95178050f58327c07"",       ""u_role"": ""teacher"", ""u_VIP"": ""vip#3-1"", ""u_lastStageId"": 3,                ""u_lastSubjectId"": 1, ""u_text_edition"": ""1"", ""u_lastSemesterId"": 22,          ""category"": ""HomePage"", ""eventKey"": ""clickTCLSubTheme"", ""eventTime"":        1594526401714, ""uuid"": ""062a27f7-da44-4808-af79-26e95e2f2c85"", ""subsectionId"":  ""194ec430-a1f4-11e8-b1c6-df78bafa5376"", ""serverTime"": 1594526410000, ""ip"":      ""106.112.84.240""}",,,,
#  "{""device"": ""bb9ff1cba21c6572"", ""imei"": ""861202045788445"", ""platform"":      ""app"", ""os"": ""android"", ""u_channel"": ""huawei"", ""productId"": ""02"",       ""netConfig"": ""wifi"", ""session"": ""a91983b8-8cba-4cb1-87ff-86227391ae37"",       ""d_app_version"": ""1.18.1"", ""d_model_brand"": ""TAS-AL00"", ""d_model_name"":     ""HUAWEI"", ""d_os_version"": ""10"", ""u_user"": ""5dd495f95178050f58327c07"",       ""u_role"": ""teacher"", ""u_VIP"": ""vip#3-1"", ""u_lastStageId"": 3,                ""u_lastSubjectId"": 1, ""u_text_edition"": ""1"", ""u_lastSemesterId"": 22,          ""category"": ""HomePage"", ""eventKey"": ""clickHPCOpen"", ""eventTime"":            1594526409997, ""uuid"": ""9a9329f3-02b8-4f8f-8774-aee520e5ac89"", ""serverTime"":    1594526410000, ""ip"": ""106.112.84.240""}",,,,

#  "{""device"": ""00070S5C970E25FW"", ""imei"": ""00070S5C970E25FW"", ""platform"":     ""app"", ""os"": ""android"", ""u_channel"": ""bbk"", ""productId"": ""02"",          ""netConfig"": ""wifi"", ""session"": ""ed781a56-55b6-4a89-a4eb-db1c743ba25d"",       ""d_app_version"": ""1.18.1"", ""d_model_brand"": ""S5"", ""d_model_name"":           ""EEBBK"", ""d_os_version"": ""9.0"", ""u_user"": ""5efd2dc368364900017d514d"",       ""u_role"": ""teacher"", ""u_VIP"": """", ""u_lastStageId"": 2, ""u_lastSubjectId"":  1, ""u_text_edition"": ""1"", ""u_lastSemesterId"": 16, ""category"":                 ""RegistGuide"", ""eventKey"": ""haltApp"", ""eventTime"": 1594526410774, ""uuid"":   ""1c6a506e-088a-4382-bbd2-a8a6f58aa3f7"", ""appDuration"": 22035, ""serverTime"":     1594526409000, ""ip"": ""43.227.139.40""}",,,,

#  "{""device"": ""f6529687a933e112"", ""imei"": """", ""platform"": ""app"", ""os"":    ""android"", ""u_channel"": ""huawei"", ""productId"": ""02"", ""netConfig"":         ""wifi"", ""session"": ""b316e069-b9e0-4575-a5ab-b2d54263fa6e"", ""d_app_version"":   ""1.18.1"", ""d_model_brand"": ""YAL-AL00"", ""d_model_name"": ""HONOR"",             ""d_os_version"": ""10"", ""u_user"": ""5f0a48ee61f7fd00013c2421"", ""u_role"":       ""teacher"", ""u_VIP"": """", ""u_lastStageId"": 3, ""u_lastSubjectId"": 1,           ""u_text_edition"": ""1"", ""u_lastSemesterId"": 22, ""category"": ""newVideo"",      ""eventKey"": ""click_Video_Arouse_Controls"", ""eventTime"": 1594526400786,          ""uuid"": ""c940ce17-1d3b-478c-a8f7-a7b15d1a788a"", ""sessionId"": ""9f087b8f-226a-   4ef0-8e30-a116676d306f"", ""sessionPublic"": ""cbab4cb2-1321-46ad-afc7-               99076078c8b5"", ""videoId"": ""b757c3f4-8b9b-11e7-8ac3-0b6c2761cb1c"",                ""serverTime"": 1594526409000, ""ip"": ""113.117.147.6""}",,,,
#  "{""device"": ""f6529687a933e112"", ""imei"": """", ""platform"": ""app"", ""os"":    ""android"", ""u_channel"": ""huawei"", ""productId"": ""02"", ""netConfig"":         ""wifi"", ""session"": ""b316e069-b9e0-4575-a5ab-b2d54263fa6e"", ""d_app_version"":   ""1.18.1"", ""d_model_brand"": ""YAL-AL00"", ""d_model_name"": ""HONOR"",             ""d_os_version"": ""10"", ""u_user"": ""5f0a48ee61f7fd00013c2421"", ""u_role"":       ""teacher"", ""u_VIP"": """", ""u_lastStageId"": 3, ""u_lastSubjectId"": 1,           ""u_text_edition"": ""1"", ""u_lastSemesterId"": 22, ""category"": ""newVideo"",      ""eventKey"": ""clickVideoResume"", ""eventTime"": 1594526397061, ""uuid"":           ""b439ad0d-c26f-4684-baf1-b7b2f0db94da"", ""sessionId"": ""9f087b8f-226a-4ef0-8e30-   a116676d306f"", ""sessionPublic"": ""cbab4cb2-1321-46ad-afc7-99076078c8b5"",          ""videoId"": ""b757c3f4-8b9b-11e7-8ac3-0b6c2761cb1c"", ""videoName"":                 ""计算必备：sinα、cosα与tanα的关系"", ""videoType"": ""course"", ""timestamp"":       268000, ""learnTime"": 210937, ""isAccord"": true, ""button"": ""1"", ""cache"":      ""false"", ""serverTime"": 1594526409000, ""ip"": ""113.117.147.6""}",,,,

# onion-event中独有的
# {'b19baaa3-c693-4b32-9179-2444caec3453'} 发现重复发送
#  "{""device"":""864079039707913"",""imei"":""864079039707913"",""platform"":""app"",   ""os"":""android"",""u_channel"":""oppokeke"",""productId"":""02"",""netConfig"":     ""wifi"",""session"":""55a3bd76-469d-4c02-ad03-5f24426a1a29"",""d_app_version"":""1.18.1"",""d_model_brand"":""OPPO R9s"",""d_model_name"":""OPPO"",""d_os_version"":""6. 0.1"",""u_user"":""5edc62fe409d190001f69b65"",""u_role"":""teacher"",""u_VIP"":"""",  ""u_lastStageId"":2,""u_lastSubjectId"":1,""u_text_edition"":""1"",                   ""u_lastSemesterId"":13,""category"":""RegistGuide"",""eventKey"":""initApp"",        ""eventTime"":1594526415454,""uuid"":""b19baaa3-c693-4b32-9179-2444caec3453"",        ""vaid"":"""",""oaid"":"""",""aaid"":"""",""isSupport"":false,""udid"":"""",""ip"":   ""36.158.30.49"",""location"":""北京市"",""ua"":""okhttp/3.12.0"",""api"":""/api/v4/  events"",""serverTime"":1594526416355}",,,,
# """
