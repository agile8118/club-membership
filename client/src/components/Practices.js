import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Input from "../reusable/Input";
import Button from "../reusable/Button";
import alert from "../lib/alert";

const Practices = () => {
  const navigate = useNavigate();
  const [practiceSessions, setPracticeSessions] = useState([]);

  // Fetch upcoming practice sessions from the server
  useEffect(() => {
    const fetchPracticeSessions = async () => {
      try {
        const response = await axios.get("/data/practices", {
          headers: { Authorization: localStorage.getItem("token") },
        });
        setPracticeSessions(response.data);
      } catch (error) {
        console.error("Error fetching practice sessions:", error);
      }
    };

    fetchPracticeSessions();
  }, []);

  // Handle sign-up for a practice session
  const handleSignUp = async (sessionId) => {
    const selectedSession = practiceSessions.find(
      (session) => session.id === sessionId
    );
    if (selectedSession) {
      alert.success(
        `Successfully signed up for the practice session on ${selectedSession.date} with Coach ${selectedSession.coach}!`
      );
    } else {
      alert.error("Practice session not found. Please try again.");
    }

    alert.success("Successfully signed up for the practice session!");
  };

  return (
    <div className="login-container">
      <h1>Upcoming Practice Sessions</h1>
      <ul>
        {practiceSessions.map((session) => (
          <li key={session.id}>
            <span>{session.date}</span>
            <span>{session.location}</span>
            <span>{session.coach}</span>
            <Button onClick={() => handleSignUp(session.id)}>Sign Up</Button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Practices;
