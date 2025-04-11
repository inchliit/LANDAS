# --- pages/7_Job_Prediction.py ---
import streamlit as st
import pandas as pd
import joblib
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import json
import time

job_assets = {	"Associate Software Engineer":{
		"image":	"assets/Associate Software Engineer.png",
		"desc":		"Your strong logical reasoning (PT1) and comfort with structured tasks (PT2) support your strength in coding and debugging. You prefer tech-based learning (LP5) and can work independently (CS4), making you ideal for developing and maintaining software systems with precision and focus."
	},
	
	"Business Process Analyst":{
		"image":	"assets/Business Process Analyst.png",
		"desc":		"Your results show a talent for pattern recognition (CS6) and systematicthinking (PT1). You enjoy data-driven decision-making (PT6) and learning through real-world business cases (LP6), making you a perfect fit for analyzing workflows and optimizing operations."
	},
	
	"Development Engineer":{
		"Image":	"assets/Development Engineer.png",
		"desc":		"With a strong drive for innovation (PT4) and technical problem-solving (CS1), you thrive in environments that challenge your creativity. You prefer visual and experimental learning (LP2, LP6) and collaborate well with others (PT5), making you suited for developing new technologies and engineering solutions."
	},

	 "Engineering Analysis Staff":{
		"image":	"assets/Engineer Analysis Staff.png",
		"desc":		"You have a methodical mindset (PT2) and excel in critical thinking and quantitative analysis (CS1). Your preference for data-focused learning (LP6) and your professional discipline (PS4) equip you to assess engineering problems and provide actionable insights."
	},

	"Engineering Management Staff/Engineer":{
		"image":	"assets/Engineering Management Staff_Engineer.png",
		"desc":		"You demonstrate leadership qualities (PS6), a preference for structured planning (PT2), and strong collaboration (PT5). With a mix of strategic thinking (PT1) and professional initiative (PS1), you're suited to lead teams, manage projects, and drive engineering performance."
	},

	"Facilities Engineering & Energy Management Engineer":{
		"image":	"assets/Facilities Engineering & Energy Management Engineer.png",
		"desc":		"You excel in technical reasoning (CS1), are hands-on in your learning (LP1), and have a focus on efficiency and sustainability (PT4). Your ability to analyze physical systems and optimize resources supports roles in facility operations and energy management."
	},

	"Government Associate":{
		"image":	"assets/Government Associate.png",
		"desc":		"Your sense of responsibility (PS3), structured thinking (PT2), and ethical mindset position you well for public service roles. You prefer learning through applied case scenarios (LP6) and work effectively within clear guidelines—perfect for regulatory, infrastructure, or policy-focused technical roles."
	},

	"Industrial Engineer":{
		"image"		:"assets/Industrial Engineer.png",
		"desc":		"Your responses highlight system optimization skills (CS5), structured planning (PT2), and a love for problem-solving (CS1). With strong organizational awareness (PS4) and the ability to analyze workflows, you’re naturally aligned with improving industrial processes and productivity."
	},

	"Instructor/ Professor":{
		"image":	"assets/Instructor_Professor.png",
		"desc":		"You demonstrate a passion for sharing knowledge (PS1), strong communication and reasoning skills (PT1, CS1), and a preference for conceptual learning (LP4). Your patience, clarity, and drive to help others grow make you an excellent educator or academic professional."
	},

	"Inventory Management, Business Process and Compliance Audit Manager":{
		"image":	"assets/Inventory Management, Business Process and Compliance Audit Manager.png",
		"desc": 		"You’re exceptionally detail-focused (PS4), organized (PT2), and systems-oriented (CS5). Your ability to enforce standards and maintain operational compliance reflects a balance of precision and strategic thinking (PT1, CS6)."
	},

	"Manufacturing Engineer":{
		"image":	"assets/Manufacturing Engineer.png",
		"desc":		"You thrive in hands-on environments (LP1) and are skilled in optimizing workflows (CS5). With strong coordination skills (CS2) and a structured mindset (PT2), you're well-equipped to oversee production efficiency and implement engineering improvements on the shop floor."
	},

	"Operational Excellence Engineer":{
		"image":	"assets/Operational Excellence Engineer.png",
		"desc":		"Your results highlight continuous improvement thinking (PT4), a knack for data-driven decisions (PT6), and a strong desire to enhance system performance (CS5). You’re a natural fit for leading Lean, Six Sigma, or Kaizen initiatives across business units."
	},

	"Operations Engineering & Management Engineer":{
		"image":	"assets/Operations Engineering & Management Engineer.png",
		"desc":		"You show a strong mix of leadership (PS6) and process optimization skills (CS5). Your comfort in structured environments (PT2) and your focus on efficiency (PT4) make you ideal for overseeing day-to-day operations and engineering team performance."
	},

	"Operations Research & Analysis Engineer":{
		"image":	"assets/Operations Research & Analysis Engineer.png",
		"desc":		"You're a data-focused thinker (PT1) with strong analytical and modeling skills (CS1, CS6). You enjoy learning through simulation and case studies (LP6), and your logical mindset suits complex problem-solving in operations and logistics systems."
	},

	"Order Management Supervisor":{
		"image":	"assets/Order Management Supervisor.png",
		"desc":		"You combine leadership and coordination skills (PS6, PT5) with a high degree of organizational discipline (PT2). Your strengths in process optimization (CS5) and collaborative problem-solving (PT1, CS3) make you ideal for managing order workflows, resolving bottlenecks, and ensuring customer satisfaction. Your learning preference for real-world scenarios (LP6) also supports your ability to adapt quickly to daily operational challenges."
	},

	"Parts Engineer":{
		"image":	"assets/Parts Engineer.png",
		"desc":		"You prefer structured, task-oriented work (PT2) and display great organizational and data accuracy (PS4). Your learning style supports visual and real-world applications (LP2, LP6), ideal for managing parts inventories and planning resource availability in technical settings."
	},

	
	"Planner":{
		"image":	"assets/Planner.png",
		"desc":		"Your responses highlight your strengths in structured thinking (PT2), attention to detail (PS4), and systematic planning (CS5). You enjoy organizing information and prefer visual and data-based learning (LP2, LP6). With strong time management (PS5) and a logical mindset (PT1), you're highly suited to forecasting, scheduling, and aligning resources efficiently across operations."
	},

		"Process Engineer":{
		"image":	"assets/Process Engineer.png",
		"desc":		"You possess a strong ability to analyze and refine systems (CS5). Your attention to detail (PS4), structured workflow preference (PT2), and applied learning strengths (LP6) support process troubleshooting and continuous improvement efforts."
	},

	"Procurement/ Purchasing Engineer":{
		"image":	"assets/Procurement_Purchasing Engineer.png",
		"desc":		"You excel at negotiation (PT5), analyzing value and cost (CS1), and managing relationships across supply networks. Your learning style favors practical applications (LP6), and your logical and organized nature supports supplier evaluation and procurement strategy."
	},

	"Product Design & Development Staff/Engineer":{
		"image":	"assets/Product Design & Development Engineer.png",
		"desc":		"You are highly creative (PT4) with strong technical analysis skills (CS1). You learn best through visual aids and hands-on experimentation (LP2, LP1), ideal for turning concepts into functioning, user-centered designs."
	},

	"Production Engineer":{
		"image":	"assets/Production Engineer.png",
		"desc":		"You thrive in structured and practical environments (PT2, LP1) and are effective in monitoring efficiency and problem-solving on the line (CS5). Your initiative and focus on results (PS1, PT4) align with the fast-paced nature of production engineering."
	},
	
	"Production Senior Supervisor":{
		"image":	"assets/Production Senior Supervisor.png",
		"desc":		"You display natural leadership and team coordination (PS6, PT5), as well as a focus on quality, safety, and productivity (PS4, PT4). You enjoy mentoring others and driving continuous improvement on the production floor."
	},

	"Project Engineer":{
		"image":	"assets/Project Engineer.png",
		"desc":		"Your responses show strength in organizing tasks (PT2), technical problem-solving (CS1), and collaborative leadership (PT5, PS6). You thrive when overseeing projects from planning to execution, balancing both engineering detail and project goals."
	},

	"Project Manager":{
		"image":	"assets/Project Manager.png",
		"desc":		"You demonstrate strategic planning abilities (PT2), professional initiative (PS1), and strong people skills (PT5). Your logical thinking (PT1) and time management (PS5) make you a natural at coordinating timelines, teams, and resources effectively."
	},

	"QA/QC or Quality & Reliability Engineering Staff/Engineer":{
		"image":	"assets/Quality & Reliability Engineering Engineer.png",
		"desc":		"You're methodical (PT2), logical (PT1), and skilled in problem-solving (CS1) and root cause analysis (CS5). You’re ideal for ensuring reliability standards and improving quality across products or systems."
	},

	
	"Safety Department Staff/Engineer":{
		"image":	"assets/Safety Engineer.png",
		"desc":		"You care deeply about precision and protocols (PS4), and your analytical mindset (PT1) supports risk assessments. With a strong sense of responsibility (PS3) and clarity in communication (PT5), you're well-equipped to ensure safety compliance and workplace wellbeing."
	},

	"Service Delivery Manager / Application Lead":{
		"image":	"assets/Service Delivery Manager.png",
		"desc":		"Your responses show strong leadership skills (PS6), attention to detail (PS4), and a preference for structured planning (PT2). You thrive in collaborative environments (PT5), take initiative (PS1), and enjoy using data to make decisions (PT1, PT6). Your ability to learn through real-world case studies (LP6) and lead strategic improvements makes you an excellent fit to lead application teams and manage client service performance."
	},

	"Shop Engineer":{
		"image":	"assets/Shop Engineer.png",
		"desc":		"You prefer hands-on learning (LP1) and are confident in physical coordination tasks (CS2). Your strengths in structured workflows (PT2) and identifying inefficiencies (CS5) help you solve production-floor problems effectively. You also show resilience in dynamic environments (PT3, PS3), making you well-suited to manage fast-paced shop operations."
	},

	"Supply Chain Management Staff/Engineer":{
		"image":	"assets/Supply Chain Management Engineer.png",
		"desc":		"Your questionnaire responses show high ability in pattern recognition and data analysis (CS6, PT1) and problem-solving (CS1, CS5). You prefer technology-driven and applied learning (LP5, LP6) and are skilled at multitasking (PS5). These strengths align well with optimizing inventory, logistics, and supply systems in real-time, collaborative environments (PT5, CS3)."
	},

	"Warehouse Staff Engineer":{
		"image":	"assets/Warehouse Staff Engineer.png",
		"desc":		"You are highly detail-oriented (PS4) and prefer structured, organized processes (PT2, LP3). Your hands-on learning (LP1) and physical coordination skills (CS2) make you ideal for managing warehouse layouts, tracking inventory, and ensuring operational accuracy. Your ability to work independently (CS4) also fits the role's routine optimization needs."
	},

	
	"Work Design & Measurement Staff/Engineer":{
		"image":	"assets/Work Design & Measurement Staff_Engineer.png",
		"desc":		"You are analytical (PT1, CS1), detail-focused (PS4), and skilled at recognizing system inefficiencies (CS5). Your responses show you prefer real-world learning (LP6) and enjoy collaborating to improve processes (PT5). This makes you ideal for evaluating task performance, improving workflows, and driving productivity improvements in organizations."
	},
}

# --- Page Config ---
st.set_page_config(page_title="Section 7 - Prediction", page_icon="💼", layout="centered")


# --- Load model, encoders, and feature order ---
model = joblib.load("job_predictor_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

with open("feature_names.txt", "r") as f:
    expected_features = [line.strip() for line in f.readlines()]

# --- Load user inputs from previous steps ---
if 'answers' in st.session_state and 'demographics' in st.session_state and 'user_info' in st.session_state:
    demo = st.session_state['demographics']
    answers = st.session_state['answers']
    user_info = st.session_state['user_info']

    # Prepare input for prediction
    input_df = pd.DataFrame([{
        "Age": demo["Age"],
        "Gender": label_encoders["Gender"].transform([demo["Gender"]])[0],
        "EDUCATION": label_encoders["EDUCATION"].transform([demo["EDUCATION"]])[0],
        **answers,
        "Feedback": st.session_state.get("feedback", ""),
        "Rating": st.session_state.get("evaluation_rating", "")

    }])
    input_df = input_df[expected_features]  # reorder columns

    # --- Prediction Logic ---
    probs = model.predict_proba(input_df)[0]
    top3_indices = probs.argsort()[-3:][::-1]
    top3_jobs = label_encoders["JOB"].inverse_transform(top3_indices)

    # ✅ Set session state so sidebar shows ✅ for Prediction
    st.session_state['P1'] = top3_jobs[0]

# --- Sidebar ---
with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Section 7 of 7")
    def check_icon(key):
        return "✅" if key in st.session_state else "⬜️"

    st.markdown(f"{check_icon('user_info')} Step 1: Personal Info")
    st.markdown(f"{check_icon('PT1')} Step 2: Personality Traits")
    st.markdown(f"{check_icon('LP1')} Step 3: Learning Preferences")
    st.markdown(f"{check_icon('CS1')} Step 4: Cognitive Strengths")
    st.markdown(f"{check_icon('PS1')} Step 5: Professional Strengths")
    st.markdown(f"{check_icon('evaluation_rating')} Step 6: Evaluation")
    st.markdown(f"{check_icon('P1')} Step 7: Prediction")

    total = sum([
        'user_info' in st.session_state,
        'PT1' in st.session_state,
        'LP1' in st.session_state,
        'CS1' in st.session_state,
        'PS1' in st.session_state,
        'evaluation_rating' in st.session_state,
        'P1' in st.session_state
    ])
    st.progress(total / 7)

st.title("🔮 Your Career Path Recommendations")
 

st.subheader("🔝 Top 3 Career Path Matches")
    for i, idx in enumerate(top3_indices):
        job_title = top3_jobs[i]
        confidence = probs[idx] * 100
        st.markdown(f"### {i+1}. **{job_title}**")
        if job_title in job_assets:
            st.image(job_assets[job_title]["image"], width=200)
            st.markdown(f"_{job_assets[job_title]['desc']}_")

    # --- Structure data for saving ---
    full_data = {
        "Name": user_info["name"],
        "Email": user_info["email"],
        "University": user_info["university"],
        "Goals": user_info["goals"],
        "Age": demo["Age"],
        "Gender": demo["Gender"],
        "EDUCATION": demo["EDUCATION"],
        **answers,
        "P1": top3_jobs[0],
        "C1": f"{probs[top3_indices[0]] * 100:.2f}%",
        "P2": top3_jobs[1],
        "C2": f"{probs[top3_indices[1]] * 100:.2f}%",
        "P3": top3_jobs[2],
        "C3": f"{probs[top3_indices[2]] * 100:.2f}%",
        "Feedback": st.session_state.get("feedback", ""),
        "Rating": st.session_state.get("evaluation_rating", "")
    }

    # --- Save to Google Sheet ---
    def save_to_gsheet(data):
        credentials_dict = dict(st.secrets["GOOGLE_CREDENTIALS"])
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
        client = gspread.authorize(creds)
        sheet = client.open("LANDAS_Responses").worksheet("Responses")

        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data["Name"],
            data["Email"],
            data["University"],
            data["Goals"],
            data["Age"],
            data["Gender"],
            data["EDUCATION"],
            *[data.get(f"PT{i}", "") for i in range(1, 7)],
            *[data.get(f"LP{i}", "") for i in range(1, 7)],
            *[data.get(f"CS{i}", "") for i in range(1, 7)],
            *[data.get(f"PS{i}", "") for i in range(1, 7)],
            data["P1"], data["C1"],
            data["P2"], data["C2"],
            data["P3"], data["C3"],
            data["Feedback"], 
            data["Rating"]

        ]
        sheet.append_row(row)

    try:
        save_to_gsheet(full_data)
        st.success("✅ Your results have been saved successfully to Google Sheets!")
    except Exception as e:
        st.error(f"❌ Error saving to Google Sheets: {e}")
        st.markdown("If you're seeing this in error, try returning to the homepage to restart.")
        if st.button("🏠 Back to Homepage"):
            st.switch_page("LANDAS.py")

    # --- Optional: Download Feature ---
    st.markdown("---")
    st.subheader("⬇️ Export Your Results")

    export_df = pd.DataFrame([{
        "Name": user_info["name"],
        "Email": user_info["email"],
        "University": user_info["university"],
        "Top Choice": top3_jobs[0],
        "Confidence 1": f"{probs[top3_indices[0]] * 100:.2f}%",
        "Second Choice": top3_jobs[1],
        "Confidence 2": f"{probs[top3_indices[1]] * 100:.2f}%",
        "Third Choice": top3_jobs[2],
        "Confidence 3": f"{probs[top3_indices[2]] * 100:.2f}%"
    }])

    csv = export_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download My Results as CSV",
        data=csv,
        file_name='LANDAS_Results.csv',
        mime='text/csv',
    )

    # --- Thank You Message ---
    st.markdown("---")
    st.success("🎉 Thank you for completing the assessment!")

    # --- Auto-clear session (after export and save) ---
    if st.button("🏠 Back to Homepage"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.success("Thank you! Redirecting you now...")
        time.sleep(1)
        st.switch_page("LANDAS.py")  # Redirect to homepage
    
    st.markdown("**Start becoming #significantlybetter. Check our free e-learning courses here.**")
    st.markdown('[🌐 Visit Our Website](https://www.asklexph.com)', unsafe_allow_html=True)

else:
    st.error("❗ Please complete all steps before this page.")
    st.markdown("If you're seeing this in error, try returning to the homepage to restart.")

    if st.button("🏠 Back to Homepage"):
        st.switch_page("LANDAS.py")