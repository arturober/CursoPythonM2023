from marshmallow import Schema, fields, validate


class ProductoSchema(Schema):
    nombre = fields.Str(
        required=True,
        error_messages={
            "required": "El nombre es obligatorio",
            "type": "El campo no tiene un formato de string",
        },
        validate=validate.Length(min=4, error="El nombre debe tener al menos 4 letras"),
    )
    precio = fields.Number(
        required=True,
        error_messages={
            "required": "El precio es obligatorio",
            "type": "El campo no tiene un formato numérico",
        },
        validate=validate.Range(min=0, error="El precio no puede ser negativo"),
    )
    imagen = fields.Str(required=True)
