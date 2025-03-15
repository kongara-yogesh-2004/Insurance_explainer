const twilio = require("twilio");

const accountSid = ""; // Twilio Account SID
const authToken = ""; // Twilio Auth Token
const twilioNumber = ""; // Your Twilio Phone Number

const client = twilio(accountSid, authToken);

async function createCall() {
  try {
    const call = await client.calls.create({
      from: twilioNumber,
      to: "+91", // Replace with the actual phone number
      record: true,
      url: "https://7b87-13-202-216-63.ngrok-free.app/twiml-response",
      method:"GET", // FastAPI endpoint for TwiML
      //recordingStatusCallback: "https://0896-13-202-216-63.ngrok-free.app/twilio-webhook", // Webhook for recording URL
      //recordingStatusCallbackMethod: "POST",
      
    });

    console.log("Call initiated! SID:", call.sid);
  } catch (error) {
    console.error("Error making the call:", error.message);
  }
}

createCall();
