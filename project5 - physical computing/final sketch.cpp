#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <DHT.h>

// Sensor toggles
bool hc_sr04_toggle = true;
bool hc_sr501_toggle = true;
bool dht_11_toggle = true;

// Sensor pins (adjust according to your wiring)
#define TRIG_PIN D1
#define ECHO_PIN D2
#define PIR_PIN D3
#define DHT_PIN D4
#define DHT_TYPE DHT11

// Sensor variables
float distance = 0;
bool movement_detected = false;
float temperature = 0;
float humidity = 0;

// WiFi credentials
const char* ssid = "xxxxxxx";
const char* password = "xxxxxxx";

// Web server
ESP8266WebServer server(80);

// DHT sensor
DHT dht(DHT_PIN, DHT_TYPE);

// HTML webpage
const char index_html[] PROGMEM = R"rawliteral(
<!DOCTYPE HTML>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="UTF-8">
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 0; 
            padding: 20px; 
            background: #f0f0f0;
        }
        .container { 
            max-width: 600px; 
            margin: 0 auto; 
            background: white; 
            padding: 20px; 
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 { 
            color: #333; 
            text-align: center;
        }
        .sensor { 
            background: #f8f9fa; 
            margin: 15px 0; 
            padding: 15px; 
            border-radius: 5px;
            border-left: 4px solid #007bff;
        }
        .sensor h2 { 
            margin-top: 0; 
            color: #007bff;
        }
        .toggle { 
            background: #007bff; 
            color: white; 
            border: none; 
            padding: 8px 15px; 
            border-radius: 4px; 
            cursor: pointer;
            margin: 5px 0;
        }
        .toggle.off { 
            background: #dc3545; 
        }
        .value { 
            font-size: 1.2em; 
            font-weight: bold; 
            margin: 10px 0;
        }
        .status { 
            padding: 5px 10px; 
            border-radius: 3px; 
            font-size: 0.9em;
        }
        .status.active { 
            background: #28a745; 
            color: white;
        }
        .status.inactive { 
            background: #6c757d; 
            color: white;
        }
    </style>
    <script>
        function toggleSensor(sensor) {
            fetch('/toggle?name=' + sensor)
                .then(response => response.text())
                .then(data => {
                    location.reload();
                });
        }
        
        function updateData() {
            fetch('/data')
                .then(response => response.json())
                .then(data => {
                    if(data.hc_sr04_toggle) {
                        document.getElementById('distance-value').innerText = data.distance + ' cm';
                    }
                    if(data.hc_sr501_toggle) {
                        let movement = data.movement_detected ? "Movement Detected" : "No Movement";
                        document.getElementById('movement-value').innerText = movement;
                        document.getElementById('movement-status').className = 
                            'status ' + (data.movement_detected ? 'active' : 'inactive');
                    }
                    if(data.dht_11_toggle) {
                        document.getElementById('temp-value').innerText = data.temperature + ' °C';
                        document.getElementById('humidity-value').innerText = data.humidity + ' %';
                    }
                });
        }
        
        setInterval(updateData, 2000);
        window.onload = updateData;
    </script>
</head>
<body>
    <div class="container">
        <h1>ESP8266 Sensor Monitor</h1>
        <p>IP Address: %IP%</p>
        
        <div class="sensor">
            <h2>HC-SR04 (Ultrasonic Distance)</h2>
            <button class="toggle %HC_SR04_CLASS%" onclick="toggleSensor('hc_sr04')">
                %HC_SR04_TOGGLE%
            </button>
            <div class="value" id="distance-value">%DISTANCE%</div>
        </div>
        
        <div class="sensor">
            <h2>HC-SR501 (PIR Motion Sensor)</h2>
            <button class="toggle %HC_SR501_CLASS%" onclick="toggleSensor('hc_sr501')">
                %HC_SR501_TOGGLE%
            </button>
            <div class="value" id="movement-value">%MOVEMENT%</div>
            <span class="status %MOVEMENT_STATUS%" id="movement-status">%MOVEMENT_STATUS_TEXT%</span>
        </div>
        
        <div class="sensor">
            <h2>DHT11 (Temperature & Humidity)</h2>
            <button class="toggle %DHT_11_CLASS%" onclick="toggleSensor('dht_11')">
                %DHT_11_TOGGLE%
            </button>
            <div class="value">Temperature: <span id="temp-value">%TEMPERATURE%</span></div>
            <div class="value">Humidity: <span id="humidity-value">%HUMIDITY%</span></div>
        </div>
    </div>
</body>
</html>
)rawliteral";

void handleRoot() {
  String html = FPSTR(index_html);

  // Replace placeholders with actual values
  html.replace("%IP%", WiFi.localIP().toString());

  // HC-SR04
  html.replace("%HC_SR04_TOGGLE%", hc_sr04_toggle ? "Turn OFF" : "Turn ON");
  html.replace("%HC_SR04_CLASS%", hc_sr04_toggle ? "" : "off");
  html.replace("%DISTANCE%", hc_sr04_toggle ? String(distance) + " cm" : "OFF");

  // HC-SR501
  html.replace("%HC_SR501_TOGGLE%", hc_sr501_toggle ? "Turn OFF" : "Turn ON");
  html.replace("%HC_SR501_CLASS%", hc_sr501_toggle ? "" : "off");
  html.replace("%MOVEMENT%", hc_sr501_toggle ? (movement_detected ? "Movement Detected" : "No Movement") : "OFF");
  html.replace("%MOVEMENT_STATUS%", hc_sr501_toggle ? (movement_detected ? "active" : "inactive") : "inactive");
  html.replace("%MOVEMENT_STATUS_TEXT%", hc_sr501_toggle ? (movement_detected ? "ACTIVE" : "INACTIVE") : "OFF");

  // DHT11
  html.replace("%DHT_11_TOGGLE%", dht_11_toggle ? "Turn OFF" : "Turn ON");
  html.replace("%DHT_11_CLASS%", dht_11_toggle ? "" : "off");
  html.replace("%TEMPERATURE%", dht_11_toggle ? String(temperature) + " °C" : "OFF");
  html.replace("%HUMIDITY%", dht_11_toggle ? String(humidity) + " %" : "OFF");

  server.send(200, "text/html", html);
}

void handleToggle() {
  String name = server.arg("name");

  if (name == "hc_sr04") {
    hc_sr04_toggle = !hc_sr04_toggle;
  } else if (name == "hc_sr501") {
    hc_sr501_toggle = !hc_sr501_toggle;
  } else if (name == "dht_11") {
    dht_11_toggle = !dht_11_toggle;
  }

  server.send(200, "text/plain", "OK");
}

void handleData() {
  String json = "{";
  json += "\"hc_sr04_toggle\":" + String(hc_sr04_toggle) + ",";
  json += "\"hc_sr501_toggle\":" + String(hc_sr501_toggle) + ",";
  json += "\"dht_11_toggle\":" + String(dht_11_toggle) + ",";
  json += "\"distance\":" + String(distance) + ",";
  json += "\"movement_detected\":" + String(movement_detected) + ",";
  json += "\"temperature\":" + String(temperature) + ",";
  json += "\"humidity\":" + String(humidity);
  json += "}";

  server.send(200, "application/json", json);
}

void setup() {
  Serial.begin(9600);

  // Initialize pins
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(PIR_PIN, INPUT);

  // Initialize DHT sensor
  dht.begin();

  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    Serial.println(WiFi.localIP());
    Serial.println(WiFi.macAddress());
    yield();
    delay(500);
    Serial.println(".");
  }

  Serial.println("\nConnected! IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println(WiFi.macAddress());

  // Setup web server routes
  server.on("/", HTTP_GET, handleRoot);
  server.on("/toggle", HTTP_GET, handleToggle);
  server.on("/data", HTTP_GET, handleData);

  // Start server
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();

  // HC-SR04 Distance Sensor
  if (hc_sr04_toggle) {
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    long duration = pulseIn(ECHO_PIN, HIGH);
    distance = duration * 0.034 / 2;  // Convert to cm

    if (distance > 400 || distance < 2) {
      distance = 0;  // Out of range
    }

    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");
  }

  // HC-SR501 PIR Sensor
  if (hc_sr501_toggle) {
    movement_detected = digitalRead(PIR_PIN);
    Serial.print("Motion: ");
    Serial.println(movement_detected ? "DETECTED" : "NO MOTION");
  }

  // DHT11 Sensor
  if (dht_11_toggle) {
    humidity = dht.readHumidity();
    temperature = dht.readTemperature();

    if (isnan(humidity) || isnan(temperature)) {
      Serial.println("Failed to read from DHT sensor!");
      humidity = 0;
      temperature = 0;
    } else {
      Serial.print("Temperature: ");
      Serial.print(temperature);
      Serial.print(" °C, Humidity: ");
      Serial.print(humidity);
      Serial.println(" %");
    }
  }

  yield();
  delay(2000);
}
