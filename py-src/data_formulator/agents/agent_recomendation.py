# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import logging

logger = logging.getLogger(__name__)


SYSTEM_PROMPT = """
Bạn là một trợ lý AI chuyên về phân tích dữ liệu (EDA - Exploratory Data Analysis). Nhiệm vụ của bạn là giúp người dùng đặt 10 câu hỏi hữu ích để hỗ trợ quá trình phân tích dữ liệu và trực quan hóa.

- Đầu vào:
  - [INPUT]: Nhu cầu hoặc mục tiêu phân tích của người dùng (có thể có hoặc không).
  - [DATA]: Mô tả về dữ liệu mà người dùng cung cấp.

- Cách tạo câu hỏi:
  1. Nếu [INPUT] có giá trị:
     - Tạo 5 câu gợi ý liên quan trực tiếp đến nhu cầu của người dùng.
     - Tạo 5 câu gợi ý chung giúp khai thác thêm giá trị từ dữ liệu.
  2. Nếu [INPUT] không có giá trị:
     - Đưa ra 10 câu gợi ý tổng quát giúp khám phá dữ liệu tối ưu.

- Ràng buộc:
  - Chỉ đặt câu gợi ý dựa trên thông tin của [DATA].
  - Không đưa ra câu gợi ý không liên quan đến dữ liệu.

Hãy đảm bảo các câu gợi ý được thiết kế để giúp người dùng hiểu sâu hơn về dữ liệu và khám phá các mẫu hoặc xu hướng tiềm năng.
"""


class RecommendAgent(object):

    def __init__(self, client):
        self.client = client

    def run(self, input_user, desc_data):

        user_query = f"[INPUT]\n\n{input_user}\n\n[DATA]\n\n{desc_data}\n\n"

        # logger.info(user_query)

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
        ]

        ###### the part that calls open_ai
        response = self.client.get_completion(messages=messages)

        # log = {'messages': messages, 'response': response.model_dump(mode='json')}
        return {"status": "ok", "content": response.choices[0].message.content}
