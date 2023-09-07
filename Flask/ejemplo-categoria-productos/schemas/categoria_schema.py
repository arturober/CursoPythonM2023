from marshmallow import Schema, fields, validate


class CategoriaSchema(Schema):
    id = fields.Int()
    nombre = fields.Str(
        required=True,
        error_messages={
            "required": "El nombre es obligatorio",
            "type": "El campo no tiene un formato de string",
        },
        validate=validate.Length(min=4, error="El nombre debe tener al menos 4 letras"),
    )
    
class CategoriaConProductosSchema(CategoriaSchema):
    productos = fields.Nested("ProductoSchema", many=True) # Lista de productos