import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

call_duration = int(input("Call Duration: "))
frequency = int(input("Frequency: "))
complaints = int(input("Complaints: "))

prediction = model.predict([[call_duration, frequency, complaints]])

if prediction[0] == 1:
    print("⚠️ Scam Call Detected")
else:
    print("✅ Safe Call")