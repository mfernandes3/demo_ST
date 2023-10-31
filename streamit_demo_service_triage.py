import streamlit as st
st.title("Service triage UI")

def determine_result(department_var, department_var_sub, department_var_sub_sub):
    department = department_var
    result = ""

    department_result_mapping = {
        "Physio/Ergo/Logo Therapeut": "PMS",
        "Reha": "PMS",
        "Radiologie": "PMS",
        "Hausarztsuche": "PMS",
        "Psyche - Arzt/Therapeut": "MSS",
    }

    if department in department_result_mapping:
        result = department_result_mapping[department]
    elif department == "Facharzt (kein HA; kein Radiologe)":
        if department_var_sub == "Ortho":
            result = "MSS"
        elif department_var_sub == "Multi":
            if department_var_sub_sub in ["Vorsorgeuntersuchung", "FA-Wechsel aus nicht-medizinschen Gründen", "war noch nicht bei FA (akut und Red flag ausgeschlossen)"]:
                result = "PMS"
            elif department_var_sub_sub == "Schneller Handlungsbedarf (Red flag)":
                result = "Handlungsempfehlung"
    elif department == "Ortho":
        if department_var_sub == "Folge eines Unfalls (BG)":
            result = "MSS"
        elif department_var_sub == "Symptomatik erst seit Tagen":
            result = "PMS"
        elif department_var_sub == "Anliegen mit schnellem Handlungsbedarf (Red flags)":
            result = "Handlungsempfehlung"
    # Add more conditions as needed for other departments.

    return result



# Create a dropdown menu for the department
departments = ["Physio/Ergo/Logo Therapeut", "Reha", "Radiologie", "Hausarztsuche", "Psyche - Arzt/Therapeut", "Facharzt (kein HA; kein Radiologe)"]
department_var = st.selectbox("Wen sucht der Patient", departments)

result = ""

# Create a nested dropdown menu for sub-department
if department_var == "Facharzt (kein HA; kein Radiologe)":
    sub_departments = ["Ortho", "Multi"]
    department_var_sub = st.selectbox("Sub-Department", sub_departments)

    # Create a nested dropdown menu for sub-sub-department
    if department_var_sub == "Multi":
        sub_sub_departments = ["Vorsorgeuntersuchung", "FA-Wechsel aus nicht-medizinschen Gründen", "war noch nicht bei FA (akut and Red flag ausgeschlossen)", "Schneller Handlungsbedarf (Red flag)"]
        department_var_sub_sub = st.selectbox("Sub-Sub-Department", sub_sub_departments)

        result = determine_result(department_var, department_var_sub, department_var_sub_sub)
    else:
        result = determine_result(department_var, department_var_sub, None)
else:
    result = determine_result(department_var, None, None)

# Create a button to determine the result
if st.button("Ergebnis bestimmen"):
    st.write("Ergebnis:", result)
