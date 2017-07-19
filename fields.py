class models:
    DO_NOTHING = None
   
    class Parent:
        def __init__(self, childName, **kwargs):
            self.classAttrs = kwargs
            if childName is "AutoField":
                self.classAttrs["type"] = "SERIAL"
            elif childName is "BooleanField":
                self.classAttrs["type"] = "BOOLEAN NOT NULL"
            elif childName is "CharField":
                if "max_length" in self.classAttrs:
                    self.classAttrs["type"] = "VARCHAR(" + str(self.classAttrs["max_length"]) + ")"
                    self.classAttrs.pop("max_length")
                else:
                    raise Exception("VARCHAR No Length")
            elif childName is "DecimalField":
                if "max_digits" in self.classAttrs and "decimal_places" in self.classAttrs:
                    self.classAttrs["type"] = "NUMERIC(" + str(self.classAttrs["max_digits"]) + "," + str(self.classAttrs["decimal_places"]) + ")"
                    self.classAttrs.pop("max_digits")
                    self.classAttrs.pop("decimal_places")
                else:
                    raise Exception("VARCHAR No Length")
            elif childName is "DurationField":
                raise NotImplementedError(childName)
            elif childName is "FilePathField":
                raise NotImplementedError(childName)
            elif childName is "FloatField":
                self.classAttrs["type"] = "DOUBLE PERCISION"
            elif childName is "IntegerField":
                self.classAttrs["type"] = "INT"
            elif childName is "IPAddressField":
                raise NotImplementedError(childName)
            elif childName is "GenericIPAddressField":
                raise NotImplementedError(childName)
            elif childName is "NullBooleanField":
                self.classAttrs["type"] = "BOOLEAN"
            elif childName is "TextField":
                self.classAttrs["type"] = "TEXT"
            elif childName is "BinaryField":
                raise NotImplementedError(childName)
            elif childName is "UUIDField":
                raise NotImplementedError(childName)
            elif childName is "RelatedField":
                raise NotImplementedError(childName)
            elif childName is "FileField":
                raise NotImplementedError(childName)
            elif childName is "ImageField":
                raise NotImplementedError(childName)
            elif childName is "CommaSeparatedImageField":
                raise NotImplementedError(childName)
            elif childName is "DateField":
                raise NotImplementedError(childName)
            elif childName is "DateTimeField":
                self.classAttrs["type"] = "TIMESTAMP WITH TIME"
            elif childName is "EmailField":
                raise NotImplementedError(childName)
            elif childName is "BigIntegerField":
                raise NotImplementedError(childName)
            elif childName is "PositiveIntegerField":
                raise NotImplementedError(childName)
            elif childName is "PositiveSmallIntegerField":
                raise NotImplementedError(childName)
            elif childName is "SlugField":
                raise NotImplementedError(childName)
                self.classAttrs["type"] = "SMALLINT"
                raise NotImplementedError(childName)
            elif childName is "TimeField":
                raise NotImplementedError(childName)
            elif childName is "URLField":
                raise NotImplementedError(childName)
            elif childName is "ForeignObject":
                raise NotImplementedError(childName)
            elif childName is "ManyToManyField":
                raise NotImplementedError(childName)
            elif childName is "OrderWrt":
                raise NotImplementedError(childName)
            elif childName is "ForeignKey":
                self.classAttrs["type"] = "FOREIGN KEY"
    class Model:
            pass

    class AutoField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class BooleanField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class CharField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)

    class DecimalField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class DurationField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class FilePathField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class FloatField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class IntegerField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class IPAddressField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class GenericIPAddressField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class NullBooleanField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class TextField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class BinaryField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class UUIDField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class RelatedField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
        
    class FileField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class ImageField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class CommaSeparatedIntegerField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class DateField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class DateTimeField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class EmailField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class BigIntegerField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class PositiveIntegerField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class PositiveSmallIntegerField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class SlugField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class SmallIntegerField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class TimeField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class URLField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class ForeignObject(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class ManyToManyField(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class OrderWrt(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
    
    class ForeignKey(Parent):
        def __init__(self, *args, **kwargs):
            models.Parent.__init__(self, type(self).__name__, **kwargs)
