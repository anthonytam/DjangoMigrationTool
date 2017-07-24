class models:
    #A small bit of hackyness, all type fields should have a space in front.
    DO_NOTHING = None
  
    @staticmethod
    def modelToTableName(modelName):
        tableName = ""
        for key, letter in enumerate(modelName):
            if letter.isupper():
                if key == 0:
                    tableName += letter.lower()
                else:
                    tableName += "_" + letter.lower()
            else:
                tableName += letter
        return tableName

    class BaseField:
        def __init__(self, **kwargs):
            self.classAttrs = kwargs
    
    class Model:
            pass

    class AutoField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            self.classAttrs["type"] = " SERIAL"
            self.classAttrs["null"] = False
        
    class BooleanField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            self.classAttrs["type"] = " BOOLEAN"
            self.classAttrs["null"] = False
        
    class CharField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            if "max_length" in self.classAttrs:
                self.classAttrs["type"] = " VARCHAR(" + str(self.classAttrs["max_length"]) + ")"
                self.classAttrs.pop("max_length")
            else:
                raise Exception("VARCHAR Missing Fields")

    class DecimalField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            if "max_digits" in self.classAttrs and "decimal_places" in self.classAttrs:
                self.classAttrs["type"] = " NUMERIC(" + str(self.classAttrs["max_digits"]) + "," + str(self.classAttrs["decimal_places"]) + ")"
                self.classAttrs.pop("max_digits")
                self.classAttrs.pop("decimal_places")
            else:
                raise Exception("DECIMAL Missing Fields")
        
    class DurationField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("FilePathField")
        
    class FilePathField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("FilePathField")
        
    class FloatField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            self.classAttrs["type"] = " DOUBLE PRECISION"
        
    class IntegerField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            self.classAttrs["type"] = " INT"
        
    class IPAddressField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("IPAddressField")
        
    class GenericIPAddressField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("GenericIPAddressField")
        
    class NullBooleanField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            self.classAttrs["type"] = " BOOLEAN"
        
    class TextField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            self.classAttrs["type"] = " TEXT"
        
    class BinaryField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("BinaryField")
        
    class UUIDField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("UUIDField")
        
    class RelatedField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("RelatedField")
        
    class FileField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("FileField")
    
    class ImageField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("ImageField")
    
    class CommaSeparatedIntegerField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("CommaSepararedIntegerField")
    
    class DateField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("DateField")
    
    class DateTimeField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            self.classAttrs["type"] = " TIMESTAMP WITH TIME ZONE"
            self.classAttrs["null"] = False
    
    class EmailField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("EmailField")
    
    class BigIntegerField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("BigIntegerField")
    
    class PositiveIntegerField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("PositiveIntegerField")
    
    class PositiveSmallIntegerField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("PositiveSmallIntegerField")
    
    class SlugField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("SlugField")
    
    class SmallIntegerField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            self.classAttrs["type"] = " SMALLINT"
    
    class TimeField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("TimeField")
    
    class URLField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("URLField")
    
    class ForeignObject(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("ForeignObject")
    
    class ManyToManyField(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("ManyToManyField")
    
    class OrderWrt(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            raise NotImplementedError("OrderWrt")
    
    class ForeignKey(BaseField):
        def __init__(self, *args, **kwargs):
            models.BaseField.__init__(self, **kwargs)
            #TODO: This may not always be INT type...
            self.classAttrs["type"] = "_id INT REFERENCES " + (models.modelToTableName(args[0]) if type(args[0]) is str else models.modelToTableName(args[0].__name__))
