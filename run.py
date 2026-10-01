import sys
from app import create_app, db, bcrypt
from app.models import User, FamilyMember, MedicalReport, MedicalBill, HealthMetric
from datetime import datetime

app = create_app()

def seed_database():
    with app.app_context():
        db.create_all()
        
        # Check if Admin exists
        admin = User.query.filter_by(email='admin@hms.com').first()
        if not admin:
            admin_pw = bcrypt.generate_password_hash('Admin@123').decode('utf-8')
            admin = User(
                name='System Admin',
                email='admin@hms.com',
                phone='+10000000000',
                password_hash=admin_pw,
                role='admin',
                is_active_account=True
            )
            db.session.add(admin)
            print("[OK] Admin account created: admin@hms.com / Admin@123")

        # Check if Demo Patient user exists
        patient = User.query.filter_by(email='patient@hms.com').first()
        if not patient:
            patient_pw = bcrypt.generate_password_hash('Patient@123').decode('utf-8')
            patient = User(
                name='John Doe',
                email='patient@hms.com',
                phone='+19876543210',
                password_hash=patient_pw,
                role='user',
                dob='1990-05-15',
                gender='Male',
                blood_group='O+',
                address='123 Health Ave, Medical City',
                emergency_contact='+19876543211',
                is_active_account=True
            )
            db.session.add(patient)
            db.session.commit()
            print("[OK] Demo Patient created: patient@hms.com / Patient@123")

            # Seed family members for demo patient
            fam1 = FamilyMember(user_id=patient.id, name='Jane Doe', relation='Spouse', age=32, gender='Female', blood_group='A+', phone='+19876543212')
            fam2 = FamilyMember(user_id=patient.id, name='Timmy Doe', relation='Son', age=8, gender='Male', blood_group='O+', phone='+19876543213')
            db.session.add_all([fam1, fam2])

            # Seed demo reports
            rep1 = MedicalReport(
                user_id=patient.id,
                title='Annual Blood Test Profile',
                hospital='City General Hospital',
                doctor='Dr. Robert Chen',
                report_type='Blood Test',
                report_date='2026-03-10',
                file_path='demo_blood_test.pdf',
                file_name='Annual_Blood_Profile_2026.pdf',
                file_size=245000
            )
            rep2 = MedicalReport(
                user_id=patient.id,
                title='Chest X-Ray Scan',
                hospital='St. Jude Radiology Center',
                doctor='Dr. Sarah Jenkins',
                report_type='X-Ray',
                report_date='2026-05-18',
                file_path='demo_xray.png',
                file_name='Chest_XRay_Scan.png',
                file_size=512000
            )
            db.session.add_all([rep1, rep2])

            # Seed demo bill
            bill1 = MedicalBill(
                user_id=patient.id,
                hospital='City General Hospital',
                bill_date='2026-03-10',
                amount=250.00,
                payment_status='Paid',
                bill_file=None
            )
            bill2 = MedicalBill(
                user_id=patient.id,
                hospital='St. Jude Pharmacy',
                bill_date='2026-05-20',
                amount=85.50,
                payment_status='Pending',
                bill_file=None
            )
            db.session.add_all([bill1, bill2])

            # Seed demo health metrics
            m1 = HealthMetric(
                user_id=patient.id,
                weight=75.0,
                height=178.0,
                bmi=23.7,
                bp_systolic=120,
                bp_diastolic=80,
                sugar_level=92.0,
                recorded_date='2026-06-01'
            )
            db.session.add(m1)

        db.session.commit()
        print("[OK] Database seeding complete.")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_database()
        
    if len(sys.argv) > 1 and sys.argv[1] == 'seed':
        print("Seeding finished.")
    else:
        print("\nHealth Management System Starting on http://127.0.0.1:5000")
        app.run(debug=True, port=5000)
