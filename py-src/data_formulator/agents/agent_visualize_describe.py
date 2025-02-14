# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import json
from data_formulator.agents.agent_utils import extract_json_objects

import logging

logger = logging.getLogger(__name__)


SYSTEM_PROMPT = '''Bạn là nhà khoa học dữ liệu để giúp người dùng mô tả dữ liệu dựa trên bảng do người dùng cung cấp.

**Quan trọng**:
- Không cần mô tả lại dữ liệu. Chỉ cần phân tích và không cần viết bất cứ điều gì khác.

Các bước bạn cần phân tích như sau:
Bước 1: Phân tích chung
Bước 2: Phân tích chi tiết từng thành phần
Bước 3: So sánh phân tích giữa các thành phần

Người dùng sẽ cung cấp cho bạn dữ liệu trong [DATA] và các trường đầu ra trong [FIELD]. Bạn cần phân tích dữ liệu và cung cấp phân tích dựa trên các trường đầu ra trong phần [FIELD].
'''



class DescVisualizeAgent(object):

    def __init__(self, client):
        self.client = client

    def run(self, output_fields, data):

        user_query = f"[FIELD]\n\n{output_fields}\n\n[DATA]\n\n{data}\n\n"

        # logger.info(user_query)

        messages = [{"role":"system", "content": SYSTEM_PROMPT},
                    {"role":"user","content": user_query}]
        
        ###### the part that calls open_ai
        response = self.client.get_completion(messages = messages)

        #log = {'messages': messages, 'response': response.model_dump(mode='json')}
        return {'status': 'ok', 'content': response.choices[0].message.content}