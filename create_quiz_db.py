import shelve

questions = [
    # Q1–Q20: Full detailed questions
    {
        "question": "What is epilepsy?",
        "options": [
            "A brain disorder causing recurring seizures",
            "A type of cancer",
            "A muscular disease"
        ],
        "answer": "A brain disorder causing recurring seizures"
    },
    {
        "question": "What should you do when someone is having a seizure?",
        "options": [
            "Put something in their mouth",
            "Hold them down",
            "Protect them from injury and stay calm"
        ],
        "answer": "Protect them from injury and stay calm"
    },
    {
        "question": "How long do most seizures last?",
        "options": [
            "Less than 2 minutes",
            "10–15 minutes",
            "Over 30 minutes"
        ],
        "answer": "Less than 2 minutes"
    },
    {
        "question": "When should you call emergency services for a seizure?",
        "options": [
            "If it lasts more than 5 minutes or it's their first seizure",
            "If the person starts sweating",
            "If the person has a history of seizures"
        ],
        "answer": "If it lasts more than 5 minutes or it's their first seizure"
    },
    {
        "question": "Can epilepsy be treated?",
        "options": [
            "No, it's lifelong and untreatable",
            "Yes, often with medication and sometimes surgery",
            "Only with herbal remedies"
        ],
        "answer": "Yes, often with medication and sometimes surgery"
    },
    {
        "question": "Is epilepsy contagious?",
        "options": [
            "Yes",
            "No",
            "Only through blood contact"
        ],
        "answer": "No"
    },
    {
        "question": "What is a common trigger for photosensitive epilepsy?",
        "options": [
            "Loud noises",
            "Flashing lights",
            "Certain foods"
        ],
        "answer": "Flashing lights"
    },
    {
        "question": "What is an 'aura' in epilepsy?",
        "options": [
            "A special type of medication",
            "A type of seizure",
            "A warning sensation before a seizure"
        ],
        "answer": "A warning sensation before a seizure"
    },
    {
        "question": "Should you restrain someone having a seizure?",
        "options": [
            "Yes, to stop their movements",
            "No, just guide them away from harm",
            "Only if they are outdoors"
        ],
        "answer": "No, just guide them away from harm"
    },
    {
        "question": "Can people with epilepsy live normal lives?",
        "options": [
            "Yes, with proper treatment and precautions",
            "No, they must stay home",
            "Only if they avoid all triggers"
        ],
        "answer": "Yes, with proper treatment and precautions"
    },
    {
        "question": "What does tonic-clonic mean in epilepsy?",
        "options": [
            "A type of medication",
            "A type of seizure with stiffening and jerking",
            "A mild headache after a seizure"
        ],
        "answer": "A type of seizure with stiffening and jerking"
    },
    {
        "question": "Is it safe to let someone sleep after a seizure?",
        "options": [
            "Yes, once they’re breathing normally and alert",
            "No, keep them awake for hours",
            "Only if they are children"
        ],
        "answer": "Yes, once they’re breathing normally and alert"
    },
    {
        "question": "Which age group can have epilepsy?",
        "options": [
            "Only children",
            "Only elderly",
            "All ages"
        ],
        "answer": "All ages"
    },
    {
        "question": "What is SUDEP in epilepsy?",
        "options": [
            "Sudden Unexpected Death in Epilepsy",
            "Severe Uncontrollable Daytime Episodes",
            "Seizure Under Drug Evaluation Program"
        ],
        "answer": "Sudden Unexpected Death in Epilepsy"
    },
    {
        "question": "What should you record during a seizure?",
        "options": [
            "Seizure length and behavior",
            "Heart rate",
            "Blood pressure"
        ],
        "answer": "Seizure length and behavior"
    },
    {
        "question": "What does an EEG test measure?",
        "options": [
            "Brain wave activity",
            "Heart rate",
            "Muscle tone"
        ],
        "answer": "Brain wave activity"
    },
    {
        "question": "What kind of doctor treats epilepsy?",
        "options": [
            "Neurologist",
            "Cardiologist",
            "Dentist"
        ],
        "answer": "Neurologist"
    },
    {
        "question": "Can skipping medication trigger a seizure?",
        "options": [
            "Yes",
            "No",
            "Only at night"
        ],
        "answer": "Yes"
    },
    {
        "question": "Is driving allowed with epilepsy?",
        "options": [
            "Yes, if seizure-free for a certain period",
            "No, never allowed",
            "Only in rural areas"
        ],
        "answer": "Yes, if seizure-free for a certain period"
    },
    {
        "question": "Do all seizures cause shaking?",
        "options": [
            "Yes",
            "No, some cause staring or confusion only",
            "Only in adults"
        ],
        "answer": "No, some cause staring or confusion only"
    },

    # Q21–Q50: Your provided normal questions
    {
        "question": "What can trigger seizures in people with epilepsy?",
        "options": ["Stress and lack of sleep", "Drinking milk", "Listening to music"],
        "answer": "Stress and lack of sleep"
    },
    {
        "question": "Can epilepsy be diagnosed with a brain scan?",
        "options": ["Yes, often with EEG or MRI", "No, only with blood tests", "Only during a seizure"],
        "answer": "Yes, often with EEG or MRI"
    },
    {
        "question": "Which lifestyle habit can help manage epilepsy?",
        "options": ["Regular sleep schedule", "Skipping meals", "Extreme exercise"],
        "answer": "Regular sleep schedule"
    },
    {
        "question": "Is epilepsy more common in men or women?",
        "options": ["Equally common", "Only in men", "Only in women"],
        "answer": "Equally common"
    },
    {
        "question": "What should you do after a person finishes a seizure?",
        "options": ["Let them rest and reassure them", "Give them water immediately", "Leave them alone"],
        "answer": "Let them rest and reassure them"
    },
    {
        "question": "Which of the following is a type of seizure?",
        "options": ["Absence seizure", "Chronic fatigue", "Muscle tear"],
        "answer": "Absence seizure"
    },
    {
        "question": "Can flashing lights trigger seizures in all people with epilepsy?",
        "options": ["No, only in some", "Yes, in everyone", "Only in children"],
        "answer": "No, only in some"
    },
    {
        "question": "Can children outgrow epilepsy?",
        "options": ["Yes, in some cases", "No, it's always permanent", "Only with surgery"],
        "answer": "Yes, in some cases"
    },
    {
        "question": "What is a seizure action plan?",
        "options": ["A document that outlines how to manage seizures", "A food chart", "A workout plan"],
        "answer": "A document that outlines how to manage seizures"
    },
    {
        "question": "What should be avoided during a seizure?",
        "options": ["Putting objects in the mouth", "Letting the person lie down", "Staying calm"],
        "answer": "Putting objects in the mouth"
    },
    {
        "question": "Do seizures always happen with warning signs?",
        "options": ["No, they can occur suddenly", "Yes, always", "Only with flashing lights"],
        "answer": "No, they can occur suddenly"
    },
    {
        "question": "Can alcohol trigger seizures?",
        "options": ["Yes", "No", "Only in women"],
        "answer": "Yes"
    },
    {
        "question": "Should you perform CPR during a seizure?",
        "options": ["No, only if they stop breathing", "Yes, always", "Only for children"],
        "answer": "No, only if they stop breathing"
    },
    {
        "question": "What does medication for epilepsy do?",
        "options": ["Helps prevent seizures", "Increases seizures", "Cures all types of epilepsy"],
        "answer": "Helps prevent seizures"
    },
    {
        "question": "Should you make a note of seizure frequency?",
        "options": ["Yes, it helps doctors adjust treatment", "No, it's unnecessary", "Only if seizures happen at night"],
        "answer": "Yes, it helps doctors adjust treatment"
    },
    {
        "question": "Are pets affected by human epilepsy?",
        "options": ["No, but they can sense seizures", "Yes, they can catch it", "Only if they sleep nearby"],
        "answer": "No, but they can sense seizures"
    },
    {
        "question": "Can certain diets help with epilepsy?",
        "options": ["Yes, like ketogenic diet", "No, diet has no effect", "Only vegetarian diets"],
        "answer": "Yes, like ketogenic diet"
    },
    {
        "question": "Should you stop epilepsy medication if seizures stop?",
        "options": ["No, only under doctor supervision", "Yes, immediately", "Only after 3 months"],
        "answer": "No, only under doctor supervision"
    },
    {
        "question": "What kind of seizure involves brief staring spells?",
        "options": ["Absence seizure", "Tonic seizure", "Myoclonic seizure"],
        "answer": "Absence seizure"
    },
    {
        "question": "Can epilepsy affect mental health?",
        "options": ["Yes, it can cause anxiety or depression", "No, only physical health", "Only in children"],
        "answer": "Yes, it can cause anxiety or depression"
    },
    {
        "question": "Can surgery cure epilepsy in some cases?",
        "options": ["Yes, if seizures come from one brain area", "No, surgery is never used", "Only if you're over 60"],
        "answer": "Yes, if seizures come from one brain area"
    },
    {
        "question": "What is status epilepticus?",
        "options": [
            "A seizure lasting more than 5 minutes or repeated without recovery",
            "A mild type of seizure",
            "A condition of calm brain activity"
        ],
        "answer": "A seizure lasting more than 5 minutes or repeated without recovery"
    },
    {
        "question": "How can schools help students with epilepsy?",
        "options": ["By having a seizure action plan", "By isolating them", "By avoiding physical activity"],
        "answer": "By having a seizure action plan"
    },
    {
        "question": "Can epilepsy be inherited?",
        "options": ["Yes, in some cases", "No, never", "Only from mothers"],
        "answer": "Yes, in some cases"
    },
    {
        "question": "What is the goal of epilepsy treatment?",
        "options": ["Control or stop seizures", "Make seizures shorter", "Avoid medication"],
        "answer": "Control or stop seizures"
    },
    {
        "question": "Is it okay to take over-the-counter medicine with epilepsy meds?",
        "options": ["Only with doctor approval", "Yes, always safe", "No, never allowed"],
        "answer": "Only with doctor approval"
    },
    {
        "question": "Can stress worsen seizures?",
        "options": ["Yes", "No", "Only in children"],
        "answer": "Yes"
    },
    {
        "question": "Do seizures always happen during the day?",
        "options": ["No, they can happen anytime", "Yes, never at night", "Only with light exposure"],
        "answer": "No, they can happen anytime"
    },
    {
        "question": "Should people with epilepsy wear medical ID?",
        "options": ["Yes, for emergencies", "No, it’s not needed", "Only if under 18"],
        "answer": "Yes, for emergencies"
    },
    {
        "question": "What is the most important step during a seizure?",
        "options": ["Keep the person safe and time the seizure", "Give them food", "Restrain their arms"],
        "answer": "Keep the person safe and time the seizure"
    }
]

with shelve.open("quiz_db") as db:
    db["questions"] = questions

print("✅ Quiz database created with 50 questions.")
