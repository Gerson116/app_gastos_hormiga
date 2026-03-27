from typing import List

from app_gastos_hormigas.src.shared.commond import dynamodb_config
from app_gastos_hormigas.src.shared.response_template import ResponseTemplate


def register_and_update_data(
        table_name: str,
        data: dict,
        multiple_data: List[dict] | None = None
):
    try:
        if multiple_data is None and data is None:
            return ResponseTemplate.error_response("La acción no puede ser realizada, por falta de data.")

        table = dynamodb_config(table_name=table_name)

        if data is not None:
            table.put_item(Item=data)
            return ResponseTemplate.success(data)


        if multiple_data is not None:
            with table.batch_writer() as batch:
                for item in data:
                    batch.put_item(Item=item)

            return ResponseTemplate.success("Proceso exitoso")
    except Exception as e:
        print(e)