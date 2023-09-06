from marshmallow import Schema, fields, validate


class TareaSchema(Schema):
    id = fields.Integer() # id es opcional
    descripcion = fields.Str(
        required=True,
        error_messages={
            "required": "La descripción es obligatoria",
            "type": "El campo no tiene un formato de string",
        },
        validate=validate.Length(
            min=6, error="La descripción debe tener al menos 6 letras"
        ),
    )
    realizada = fields.Boolean(
        required=True,
        error_messages={
            "required": "El campo 'realizada' es obligatorio",
            "type": "El campo no es un booleano",
        },
    )