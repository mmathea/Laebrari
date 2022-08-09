from datetime import date, datetime, timedelta
from user_library.models import  Book, BookTransaction, UserLibrary
from rest_framework import serializers


class UserLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLibrary
        fields = '__all__'
    
    def create(self, validated_data):
        instance, created = UserLibrary.objects.get_or_create(**validated_data)
        if not created:
            raise serializers.ValidationError({'message': instance.name + ' already exists.'})
        return instance

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def create(self, validated_data):
        instance, created = Book.objects.get_or_create(**validated_data)
        if not created:
            raise serializers.ValidationError({'message': instance.title + ' already exists.'})
        return instance

class LibBookSerializer(serializers.ModelSerializer):
    library = UserLibrarySerializer()
    class Meta:
        model = Book
        fields = ['title', 'author', 'date_acquired', 'owner', 'memo', 'genre', 'book_condition', 'borrowing_price', 'selling_price', 'available_to_borrow', 'isbn', 'library']

class BookTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTransaction
        fields = ['book', 'transaction_type', 'patron', 'end_of_transaction']
    
    def create(self, validated_data): 
        if validated_data['transaction_type'] == 'LOAN' and 'end_of_transaction' not in validated_data:
            validated_data['end_of_transaction'] = date.today() + timedelta(days=14)
            print('Creating transaction: '+ str(validated_data))
            # validated_data = self.validated_data
        return BookTransaction.objects.create(**validated_data)

