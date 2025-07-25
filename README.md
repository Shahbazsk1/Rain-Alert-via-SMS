# 🌧️ Rain-Alert-via-SMS
<h2>📌 Project Description</h2>
<p>This Python project fetches weather forecast data using the OpenWeatherMap API, checks if it is going to rain in the next few hours, and sends a rain alert message via Twilio SMS if rain is predicted. It's useful for personal weather alerts so you never forget to carry an umbrella.</p>
<h3>🧱 Modules/Libraries Used</h3>
<ul>
  <li><strong>requests :</strong>	To make HTTP requests to the OpenWeatherMap API and retrieve weather forecast data.</li>
  <li><strong>twilio.rest :</strong>vFrom the Twilio Python SDK; used to send SMS messages to a phone number</li>
</ul>
<h3>APIs and Services Used</h3>
<ol>
  <li>🌐 OpenWeatherMap API
    <ul>
      <li><strong>Purpose:</strong> Get 5-day/3-hour weather forecast.</li>
      <li>API Endpoint:<br>
        <p>https://api.openweathermap.org/data/2.5/forecast</p>
      </li>
      <li>Docs:<br>
        <a href="https://openweathermap.org/forecast5" target="_blank">OpenWeatherMap Forecast API Docs</a>
      </li>
    </ul>
  </li><br>
  <li>📲 Twilio API
    <ul>
      <li><strong>Purpose:</strong> Send SMS programmatically to a phone number.</li>
      <li><strong>Website:</strong><br>
        <a href="https://www.twilio.com/" target="_blank">Twilio</a>
      </li><br>
      <li><strong>Python SDK Documentation:</strong><br>
        <a href="https://www.twilio.com/docs/libraries/python" target="_blank">Twilio Python Helper Library</a>
      </li>
    </ul>
  </li>
</ol>
<h3>Twilio Setup Guide (for SMS Sending)</h3>
<p><strong>Step 1: Create a Twilio Account</strong></p>
<ol>
  <li>Go to <a href="https://www.twilio.com/" target="_blank">https://www.twilio.com/</a></li>
  <li>Click on Sign Up (if you don't have an account) or Log In</li>
  <li>Verify your email and phone number.</li>
</ol>
<p><strong>📱 Step 2: Get a Twilio Phone Number</strong></strong></p>
<ol>
  <li>Go to your <a href="https://console.twilio.com/" target="_blank">Twilio Console Dashboard</a></li>
  <li>Click on Get a Twilio Phone Number</li>
  <li>Choose a number with SMS capability</li>
  <li>Note down the phone number — you'll use this as the from_ number in your code.</li>
</ol>
<p><strong>🔐 Step 3: Get Twilio Account SID and Auth Token</strong></p>
<ol>
  <li>From the Dashboard, copy the following:
    <ul>
      <li><strong>Account SID →</strong> used for authentication</li>
      <li><strong>Auth Token →</strong> keep this private</li>
    </ul>
  </li>
  <li>You’ll use these in your code:</li><br>
  <p>account_sid = "YOUR_TWILIO_ACCOUNT_SID"<br>
    auth_token = "YOUR_TWILIO_AUTH_TOKEN"</p>
</ol>
<h3>💬 Step 4: Verify Recipient Phone Number (for Trial Account)</h3>
<p>If you're using a <strong>free trial account</strong>, Twilio <strong>only allows SMS to verified phone numbers:</strong></p>
<ol>
   <li>Go to: <a href="https://console.twilio.com/us1/verified-caller-ids/phone-numbers" target="_blank">Verified Caller IDs</a>
   <li>Click <strong>Add a New Verified Number</strong></li>
   <li>Enter your personal phone number and verify it via OTP.</li>
</ol>












