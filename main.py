import uuid
import service.contact_service as service


def main():
    contact_service = service.Contact_Service()
    value = {
            "id": str(uuid.uuid4()),
            "name": "tirtahakim",
            "email":"tirtahakim22@gmail.com",
            "phone": "823121921313",  # Provide the phone number in digit-only format
            "address": "St Malioboro",
            "category": "FRIENDS"
    }
    contact_service.create_contact(contact=value)



if __name__ == '__main__':
    main()
