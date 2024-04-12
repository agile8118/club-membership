import React, { useState, useEffect } from "react";
import axios from "axios";
import Button from "../reusable/Button";
import InlineLoading from "../reusable/InlineLoading";
import alert from "../lib/alert";

const Practices = () => {
  const [practiceSessions, setPracticeSessions] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchPracticeSessions = async () => {
    try {
      setLoading(true);
      const response = await axios.get("/practices", {
        headers: { Authorization: localStorage.getItem("token") },
      });
      setPracticeSessions(response.data);
    } catch (error) {
      if (err.response.data.error) {
        alert(err.response.data.error, "error");
      }
    }
    setLoading(false);
  };

  // Fetch upcoming practice sessions from the server
  useEffect(() => {
    fetchPracticeSessions();
  }, []);

  // Handle sign-up for a practice session
  const handleSignUp = async (sessionId) => {
    try {
      const response = await axios.post(
        "/practice-signup",
        { session_id: sessionId },
        {
          headers: { Authorization: localStorage.getItem("token") },
        }
      );

      fetchPracticeSessions();
      alert(response.data.message, "success");
    } catch (err) {
      if (err.response.data.error) {
        alert(err.response.data.error, "error");
      }
    }
  };

  const handlePay = async (sessionId) => {
    // find the session with the given id
    const session = practiceSessions.find(
      (session) => session.id === sessionId
    );
    if (
      window.confirm(
        `Are you sure you want to pay for the ${session.name} session on ${session.date} ${session.time}? If you confirm, it's like as if you have connected to a payment gateway and completed the payment. Feature coming soon!`
      )
    ) {
      try {
        const response = await axios.post(
          "/practice-pay",
          { session_id: sessionId },
          {
            headers: { Authorization: localStorage.getItem("token") },
          }
        );

        fetchPracticeSessions();
        alert(response.data.message, "success");
      } catch (err) {
        if (err.response.data.error) {
          alert(err.response.data.error, "error");
        }
      }
    }
  };

  const handleCancelSession = async (sessionId) => {
    try {
      const response = await axios.post(
        "/cancel-practice-signup",
        { session_id: sessionId },
        {
          headers: { Authorization: localStorage.getItem("token") },
        }
      );

      fetchPracticeSessions();
      alert(response.data.message, "success");
    } catch (err) {
      if (err.response.data.error) {
        alert(err.response.data.error, "error");
      }
    }
  };

  const renderUpcomingSessions = () => {
    const currentDate = new Date();

    let sessions = practiceSessions.map((session) => {
      const sessionDate = new Date(`${session.date} ${session.time}`);

      if (sessionDate > currentDate) {
        return (
          <div className="session" key={session.id}>
            <div className="session__name">{session.name}</div>
            <div className="session_coach">By {session.coach}</div>
            <div>
              {session.date} {session.time}
            </div>
            <div className="session_actions">
              {!session.member_paid && session.member_attend && (
                <Button
                  color="red"
                  onClick={() => handleCancelSession(session.id)}
                >
                  Cancel Attendance
                </Button>
              )}

              {!session.member_attend && (
                <Button color="blue" onClick={() => handleSignUp(session.id)}>
                  Sign Up
                </Button>
              )}

              {session.member_attend && !session.member_paid && (
                <Button color="green" onClick={() => handlePay(session.id)}>
                  Pay ${session.price}
                </Button>
              )}

              {session.member_paid && (
                <span>Payment of ${session.price} completed.</span>
              )}
            </div>
          </div>
        );
      }
    });

    // remove all undefined values
    sessions = sessions.filter((session) => session);

    if (sessions.length === 0) {
      return (
        <p className="u-margin-bottom-1">
          No upcoming practice sessions found.
        </p>
      );
    }
  };

  const renderPastSessions = () => {
    const currentDate = new Date();

    let sessions = practiceSessions.map((session) => {
      const sessionDate = new Date(`${session.date} ${session.time}`);

      if (sessionDate < currentDate) {
        return (
          <div className="session" key={session.id}>
            <div className="session__name">{session.name}</div>
            <div className="session_coach">By {session.coach}</div>
            <div>
              {session.date} {session.time}
            </div>
            <div className="session_actions">
              {session.member_attend && !session.member_paid && (
                <Button color="green" onClick={() => handlePay(session.id)}>
                  Pay ${session.price}
                </Button>
              )}

              {session.member_paid && (
                <span>Payment of ${session.price} completed.</span>
              )}
            </div>
          </div>
        );
      }
    });

    // remove all undefined values
    sessions = sessions.filter((session) => session);

    if (sessions.length === 0) {
      return (
        <p className="u-margin-bottom-1">No past practice sessions found.</p>
      );
    }

    return sessions;
  };

  if (loading) {
    return (
      <div className="sessions-container">
        <div className="u-text-center">
          <InlineLoading color="gray" />
        </div>
      </div>
    );
  }

  return (
    <div className="sessions-container">
      <h1>Upcoming Practice Sessions:</h1>
      <div>{renderUpcomingSessions()}</div>
      <h1>Past Practice Sessions:</h1>
      <div>{renderPastSessions()}</div>
    </div>
  );
};

export default Practices;
