from db import models


# Functions

def create_report(patient):
    # get the appointments
    appointments = models.Appointment.objects.filter(patient=patient).all()
    # get the examinations
    examinations = models.Examination.objects.filter(appointment__in=appointments).all()
    # get the medicines
    medicines = models.Medicine.objects.all()

    # create report pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Patient Report')
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 10, 'Patient Name: ' + patient.name)
    pdf.ln(10)
    pdf.cell(40, 10, 'Patient ID: ' + patient.id)
    pdf.ln(10)
    pdf.cell(40, 10, 'Patient Age: ' + str(patient.age))
    


    return report

