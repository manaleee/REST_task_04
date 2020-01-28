from rest_framework import serializers

from .models import Flight, Booking

from django.contrib.auth.models import User 


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']




# register 


class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name']


		def create(self, validated_data):
			username = validated_data.get("username")			
			password = validated_data.get("password")
			first_name = validated_data.get("first_name")
			last_name = validated_data.get("last_name")


			new_user = User(username= username,    first_name= first_name,    last_name= last_name )

			# new_user = User(username= username)
			# new_user.first_name = first_name
			# new_user.last_name = last_name
			
			



			new_user.set_password(password)

			new_user.save()

			return validated_data



