import json
from persistant.sqlite_db_manager import save_search_history, fetch_search_history
from service.retrive import retrive
def lambda_handler(event, context):
    headers = {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
            }
    # 경로별 분기 처리
    # CORS preflight 요청에 대한 처리
    if event['requestContext']['http']['method'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                'Access-Control-Allow-Origin': '*',  # 필요한 경우 특정 도메인으로 제한 가능
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
            },
            'body': ''
        }
    path = event['requestContext']['http']['path']
    
    if path == '/resgistPerson':
        # 매물 등록
        
        return {
            'statusCode': 200,
            'body': body,
            'headers': headers
        }

    if path == '/retrive':
        # 매물 검색 및 추천
        body = json.loads(event['body'])
        
        response = retrive(body)
        
        return {
            'statusCode': 200,
            'body': response,
            'headers': headers
        }

            
    if path == '/saveHistory':
        # 검색 기록을 저장
        body = json.loads(event['body'])
        
        # 검색 기록 저장
        save_search_history(instance_type, region, price)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': '검색이력 저장완료'}),
            'headers':headers
            
        }

    elif path == '/searchHistory':
        # 검색 기록을 조회
        search_history = fetch_search_history()
        # 검색 기록 데이터를 json으로 파싱작업
        body = []
        
        return {
            'statusCode': 200,
            'body': body,
            'headers':headers
        }

    else:
        # 정의되지 않은 경로 처리
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Not Found'}),
            'headers': headers
        }
