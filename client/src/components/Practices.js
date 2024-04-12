import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { AppContext } from "../index";
import Input from "../reusable/Input";
import Button from "../reusable/Button";
import alert from "../lib/alert";

const Practices = () => {
  const navigate = useNavigate();
  const [practiceSessions, setPracticeSessions] = useState([]);

  const { userId } = useContext(AppContext);

  // Fetch upcoming practice sessions from the server
  useEffect(() => {
    const fetchPracticeSessions = async () => {
      try {
        const response = await axios.get("/practices", {
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

  const renderUpcomingSessions = () => {
    // if (practiceSessions.length === 0) {
    //   return <p>No upcoming practice sessions found.</p>;
    // }

    const currentDate = new Date();

    return practiceSessions.map((session) => {
      const sessionDate = new Date(`${session.date} ${session.time}`);

      if (sessionDate > currentDate) {
        // only render if session.date and session.time are in the future
        // (compare to current date and time)
        // render the session details

        return (
          <div className="session" key={session.id}>
            <div className="session__name">{session.name}</div>
            <div className="session_coach">By {session.coach}</div>
            <div>
              {session.date} {session.time}
            </div>
            <div className="session_actions">
              {/* {session.mem} */}
              <Button color="blue" onClick={() => handleSignUp(session.id)}>
                Sign Up
              </Button>
              <Button color="green" onClick={() => handleSignUp(session.id)}>
                Pay
              </Button>
            </div>
          </div>
        );
      }
    });
  };

  const renderPastSessions = () => {
    // if (practiceSessions.length === 0) {
    //   return <p>No upcoming practice sessions found.</p>;
    // }

    const currentDate = new Date();

    return practiceSessions.map((session) => {
      const sessionDate = new Date(`${session.date} ${session.time}`);

      if (sessionDate < currentDate) {
        // only render if session.date and session.time are in the future
        // (compare to current date and time)
        // render the session details

        return (
          <div className="session" key={session.id}>
            <div className="session__name">{session.name}</div>
            <div className="session_coach">By {session.coach}</div>
            <div>
              {session.date} {session.time}
            </div>
            {/* <Button onClick={() => handleSignUp(session.id)}>Sign Up</Button> */}
          </div>
        );
      }
    });
  };

  return (
    <div className="sessions-container">
      <h1>Upcoming Practice Sessions:</h1>
      {/* <input
        type="time"
        onChange={(e) => {
          console.log(e.target.value);
        }}
      /> */}
      <div>{renderUpcomingSessions()}</div>
      <h1>Past Practice Sessions:</h1>
      <div>{renderPastSessions()}</div>
    </div>
  );
};

export default Practices;
