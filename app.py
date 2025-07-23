from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Emergency guide data with 4-language support
steps_data = [
    {
        "step": 1,
        "image": "step1.png",
        "text": {
            "en": "Stay calm. Stay calm and observe the individual having a seizure.",
            "zh": "保持冷静。保持冷静，观察癫痫发作的人。",
            "ms": "Bertenang. Kekal tenang dan perhatikan individu yang mengalami sawan.",
            "ta": "அமைதியாக இருங்கள். அமைதியாக இருங்கள், நபருக்கு வலிப்பு ஏற்படுவதைக் கவனியுங்கள்."
        },
        "audio": {
            "en": "step1_en.mp3",
            "zh": "step1_zh.mp3",
            "ms": "step1_ms.mp3",
            "ta": "step1_ta.mp3"
        }
    },
    {
        "step": 2,
        "image": "step2.png",
        "text": {
            "en": "Protect their head. Place something soft under their head.",
            "zh": "保护好他们的头部。在他们的头下放一些柔软的东西。",
            "ms": "Lindungi kepala. Letakkan sesuatu yang lembut di bawah kepala mereka.",
            "ta": "அவர்களின் தலையைப் பாதுகாக்கவும். அவர்களின் தலைக்குக் கீழே மென்மையான ஒன்றை வைக்கவும்."
        },
        "audio": {
            "en": "step2_en.mp3",
            "zh": "step2_zh.mp3",
            "ms": "step2_ms.mp3",
            "ta": "step2_ta.mp3"
        }
    },
    {
        "step": 3,
        "image": "step3.png",
        "text": {
            "en": "Remove hazards. Keep hard or sharp objects away from their surroundings.",
            "zh": "消除危险。将坚硬或尖锐的物体远离周围环境。",
            "ms": "Alihkan bahaya. Jauhkan objek keras atau tajam dari sekeliling mereka.",
            "ta": "ஆபத்துகளை நீக்குங்கள். கடினமான அல்லது கூர்மையான பொருட்களை அவற்றின் சுற்றுப்புறங்களிலிருந்து விலக்கி வைக்கவும்."
        },
        "audio": {
            "en": "step3_en.mp3",
            "zh": "step3_zh.mp3",
            "ms": "step3_ms.mp3",
            "ta": "step3_ta.mp3"
        }
    },
    {

        "step": 4,
        "image": "step3.png",
        "text": {
            "en": "Wait for the seizure to stop. Do not hold them or put anything in their mouth.",
            "zh": "等待癫痫发作停止。不要抱住孩子或将任何东西放入孩子嘴里。",
            "ms": "Tunggu sawan berhenti. Jangan tahan mereka atau masukkan apa-apa ke dalam mulut mereka.",
            "ta": "வலிப்பு நிற்கும் வரை காத்திருங்கள். அவர்களைப் பிடிக்கவோ அல்லது அவர்களின் வாயில் எதையும் வைக்கவோ வேண்டாம்."
        },
        "audio": {
            "en": "step4_en.mp3",
            "zh": "step4_zh.mp3",
            "ms": "step4_ms.mp3",
            "ta": "step4_ta.mp3"
        }
    },
    {

        "step": 5,
        "image": "step3.png",
        "text": {
            "en": "Check the time. If the seizure lasts more than 5 minutes, seek medical help.",
            "zh": "检查时间。如果癫痫发作持续超过5分钟，请就医。",
            "ms": "Periksa masa. Jika sawan melebihi 5 minit, hubungi bantuan perubatan.",
            "ta": "நேரத்தைச் சரிபார்க்கவும். வலிப்பு 5 நிமிடங்களுக்கு மேல் நீடித்தால், மருத்துவ உதவியை நாடுங்கள்."
        },
        "audio": {
            "en": "step5_en.mp3",
            "zh": "step5_zh.mp3",
            "ms": "step5_ms.mp3",
            "ta": "step5_ta.mp3"
        }
    },
    {

        "step": 6,
        "image": "step3.png",
        "text": {
            "en": "Monitor after a seizure. Help them recover and stay with them until they are fully conscious.",
            "zh": "癫痫发作后进行监护。帮助他们恢复，并陪伴他们直到他们完全清醒。",
            "ms": "Pantau selepas sawan. Bantu mereka pulih dan kekal bersama mereka sehingga sedar sepenuhnya.",
            "ta": "வலிப்புக்குப் பிறகு கண்காணிக்கவும். அவர்கள் குணமடைய உதவுங்கள், அவர்கள் முழுமையாக சுயநினைவு அடையும் வரை அவர்களுடன் இருங்கள்."
        },
        "audio": {
            "en": "step6_en.mp3",
            "zh": "step6_zh.mp3",
            "ms": "step6_ms.mp3",
            "ta": "step6_ta.mp3"
        }
    }
]



@app.route("/")
def home():
    return render_template("home.html")





from flask import request, session, render_template

@app.route('/chatbot')
def chatbot():
    lang = request.args.get('lang')
    if lang:
        session['chat_lang'] = lang  # save language in session
    return render_template('chatbot.html')
app.secret_key = 'your_secret_key'

@app.route("/video")
def video():
    section = request.args.get("section", "")
    return render_template("video.html", section=section)

@app.route("/infographic")
def infographic():
    section = request.args.get("section", "")
    return render_template("infographic.html", section=section)

@app.route("/cards")
def cards():
    section = request.args.get("section", "")
    return render_template("cards.html", section=section)

import shelve

app.secret_key = 'seizuresmart-key'

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    with shelve.open("quiz_db") as db:
        questions = db["questions"]

    if "current_q" not in session:
        session["current_q"] = 0
        session["score"] = 0

    current_q = session["current_q"]
    feedback = None

    if request.method == 'POST':
        selected = request.form.get("answer")
        correct_answer = questions[current_q]["answer"]

        if selected == correct_answer:
            session["score"] += 1
            session["current_q"] += 1
            feedback = "Correct!"
        else:
            feedback = "Wrong! Try again."

        current_q = session["current_q"]

    if current_q >= len(questions):
        score = session["score"]
        session.clear()
        return render_template("quiz_result.html", score=score, total=len(questions))

    question = questions[current_q]
    return render_template("quiz.html", question=question, q_num=current_q + 1, total=len(questions), feedback=feedback)

from flask import request, jsonify

@app.route('/chatbot_api', methods=['POST'])
def chatbot_api():
    data = request.get_json()
    user_message = data.get('message', '').lower()

    # Keyword-based response dictionary
    responses = {
        "seizure": "A seizure is caused by abnormal brain activity. Stay calm and ensure the person is safe.",
        "steps": "There are 6 main steps. Start by staying calm and ensuring safety. Would you like to begin the guide?",
        "symptoms": "Common symptoms include jerking movements, loss of awareness, confusion, and staring spells.",
        "first aid": "Stay calm, protect the person's head, and don't put anything in their mouth.",
        "emergency": "Call emergency services if the seizure lasts more than 5 minutes or if it's their first seizure.",
        "help": "I'm here to help. You can ask about seizures, symptoms, steps, or what to do in an emergency.",
        "head": "Protect their head by placing something soft underneath it during a seizure.",
        "sharp objects": "Move away any hard or sharp objects nearby to prevent injury.",
        "duration": "If a seizure lasts more than 5 minutes, seek medical help immediately.",
        "mouth": "Do not put anything in their mouth during a seizure. It can cause choking.",
        "after seizure": "Stay with the person, help them recover, and ensure they are fully conscious.",
        "safe position": "Turn the person onto their side to keep their airway clear.",
        "breathing": "Check if the person is breathing after the seizure. If not, seek emergency help.",
        "unconscious": "Stay with them and monitor breathing until help arrives.",
        "call ambulance": "Yes, call 995 or emergency services if the seizure continues or is their first.",
        "convulsion": "Convulsions are strong, involuntary muscle contractions – common in tonic-clonic seizures.",
        "aura": "Some people experience an 'aura' – a warning before a seizure, like strange smells or feelings.",
        "epilepsy": "Epilepsy is a neurological condition with recurring seizures. It's manageable with medication.",
        "doctor": "It's important to see a doctor for diagnosis and treatment if seizures occur.",
        "medication": "Anti-seizure medications are often used to control seizures. Follow a doctor's advice.",
        "lights": "Flashing lights can trigger seizures in some people (photosensitive epilepsy).",
        "noises": "Loud or sudden noises are not common triggers, but stress and fatigue can contribute.",
        "trigger": "Common triggers: lack of sleep, stress, illness, or flashing lights.",
        "stress": "Stress is a common seizure trigger. Practice relaxation and self-care.",
        "sleep": "Lack of sleep can increase the risk of seizures. Aim for consistent rest.",
        "hydration": "Staying hydrated and eating regularly helps manage seizure risk.",
        "child": "Children can have seizures for many reasons. Stay calm and seek medical advice.",
        "school": "Inform teachers and caregivers about a child’s condition and what to do during a seizure.",
        "pregnancy": "Women with epilepsy can have safe pregnancies with proper medical care.",
        "driving": "Driving after a seizure may require a doctor’s clearance, depending on local laws.",
        "sports": "People with epilepsy can enjoy sports with precautions and proper support.",
        "safety": "Always ensure the person's environment is safe during and after a seizure.",
        "language": "You can switch the app language on the home page or chatbot menu.",
        "guide": "Tap on the emergency guide tab to view the seizure response steps.",
        "quiz": "Try our gamified quiz to learn seizure response skills interactively!",
        "offline": "If offline, use the fallback guide with images and local audio.",
        "multilingual": "This chatbot supports English, 中文, Bahasa Melayu, தமிழ்.",
        "autoplay": "Turn on autoplay to hear the steps read aloud hands-free.",
        "audio": "Each step includes audio in 4 languages. Make sure your volume is on.",
        "certification": "Complete the quiz to earn a 'CareLink Certified' badge.",
        "badge": "Finish all steps and pass the quiz to receive your safety badge!",
        "volunteer": "Want to help others? Contact us to volunteer or support epilepsy education.",
        "community": "Join our community events to raise awareness and learn more.",
        "ngo": "We collaborate with NGOs to spread awareness about seizure first aid.",
        "donate": "Your donations help support education and emergency care outreach.",
        "voice": "Voices used in this app are real recordings in all supported languages.",
        "ai": "Our AI helps guide you through seizure steps based on your language choice.",
        "handsfree": "Hands-free mode allows the steps to play automatically without interaction.",
        "settings": "Change your language or enable autoplay in the settings menu.",
        "replay": "You can replay any step by tapping the speaker icon.",
        "repeat": "Would you like me to repeat that?",
        "start guide": "Sure, launching the emergency guide now...",
        "bye": "Stay safe! Let me know if you need help again.",
        "thank you": "You're welcome! I'm always here to help."
    }

    # Check for keyword match
    reply = None
    for keyword, response in responses.items():
        if keyword in user_message:
            reply = response
            break

    # Default fallback message
    if not reply:
        reply = "I'm still learning. Try keywords like 'seizure', 'steps', or 'symptoms'."

    return jsonify({"reply": reply})

@app.route("/learn")
def learn():
    return render_template("learn.html")


@app.route("/guide")
def start_guide():
    lang = request.args.get("lang", "en")
    autoplay = request.args.get("autoplay", "false")
    handsfree = request.args.get("handsfree", "false")
    return redirect(url_for("guide_step", step_num=1, lang=lang, autoplay=autoplay, handsfree=handsfree))

@app.route("/guide/<int:step_num>")
def guide_step(step_num):
    lang = request.args.get("lang", "en")
    autoplay = request.args.get("autoplay", "false")
    handsfree = request.args.get("handsfree", "false")
    if 1 <= step_num <= len(steps_data):
        step = steps_data[step_num - 1]
        audio_file = step["audio"].get(lang, step["audio"]["en"])
        return render_template("guide_step.html",
                               step=step,
                               lang=lang,
                               audio_file=audio_file,
                               autoplay=autoplay,
                               handsfree=handsfree,
                               current_step=step_num,
                               total_steps=len(steps_data))
    return "Step not found", 404

if __name__ == "__main__":
    app.run(debug=True)


