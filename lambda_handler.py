import pymysql
import json

def Sql_connection():
    mydb = pymysql.connect(
        host='localhost',
        user='root',
        password='shiv',
        database='py_db',
        cursorclass=pymysql.cursors.DictCursor
    )

    mycursor = mydb.cursor()
    return mycursor



def execute_query(query, cursor):
    cursor.execute(query)
    return cursor.fetchall()



def All_teacher_data(c, teacher_id=None):
    print(teacher_id, "iiiiiii")
    if teacher_id is not None:
        query = "SELECT * FROM teacher WHERE ID={}".format(teacher_id)
        c.execute(query)
        return c.fetchall()
    else:
        query = "SELECT * FROM teacher"
        c.execute(query)
        return c.fetchall()
    



def lambda_handler(event, context):
    print(event['path'])
    if event['path'] == f'/teacher':
        c = Sql_connection()  
        result = All_teacher_data(c)
        c.close()
    
    teacher_id=event['pathParameters']
    if event['path'] ==  f'/teacher/{teacher_id}':
        if teacher_id is not None:
            c = Sql_connection()  
            result = All_teacher_data(c, teacher_id)
            c.close()
        

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }





event = {
  "resource": "/",
  "path": "teacher/",
  "httpMethod": "POST",
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.8,en;q=0.6,zh-CN;q=0.4",
    "cache-control": "max-age=0",
    "CloudFront-Forwarded-Proto": "https",
    "CloudFront-Is-Desktop-Viewer": "true",
    "CloudFront-Is-Mobile-Viewer": "false",
    "CloudFront-Is-SmartTV-Viewer": "false",
    "CloudFront-Is-Tablet-Viewer": "false",
    "CloudFront-Viewer-Country": "GB",
    "content-type": "application/x-www-form-urlencoded",
    "Host": "j3ap25j034.execute-api.eu-west-2.amazonaws.com",
    "origin": "https://j3ap25j034.execute-api.eu-west-2.amazonaws.com",
    "Referer": "https://j3ap25j034.execute-api.eu-west-2.amazonaws.com/dev/",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Via": "2.0 a3650115c5e21e2b5d133ce84464bea3.cloudfront.net (CloudFront)",
    "X-Amz-Cf-Id": "0nDeiXnReyHYCkv8cc150MWCFCLFPbJoTs1mexDuKe2WJwK5ANgv2A==",
    "X-Amzn-Trace-Id": "Root=1-597079de-75fec8453f6fd4812414a4cd",
    "X-Forwarded-For": "50.129.117.14, 50.112.234.94",
    "X-Forwarded-Port": "443",
    "X-Forwarded-Proto": "https"
  },
  "queryStringParameters": None,
  "pathParameters": 2,
  "stageVariables": None,
  "requestContext": {
    "path": "/dev/",
    "accountId": "125002137610",
    "resourceId": "qdolsr1yhk",
    "stage": "dev",
    "requestId": "0f2431a2-6d2f-11e7-b799-5152aa497861",
    "identity": {
      "cognitoIdentityPoolId": None,
      "accountId": None,
      "cognitoIdentityId": None,
      "caller": None,
      "apiKey": "",
      "sourceIp": "50.129.117.14",
      "accessKey": None,
      "cognitoAuthenticationType": None,
      "cognitoAuthenticationProvider": None,
      "userArn": None,
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
      "user": None
    },
    "resourcePath": "/",
    "httpMethod": "POST",
    "apiId": "j3azlsj0c4"
  },
  "body": "{'Key':'Value'}",
  "isBase64Encoded": False
}

data = lambda_handler(event, context=None)
print(data)
