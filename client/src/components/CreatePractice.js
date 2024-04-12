import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { AppContext } from "../index";
import { useNavigate, Link } from "react-router-dom";
import Input from "../reusable/Input";
import Button from "../reusable/Button";
import alert from "../lib/alert";

const CreatePractice = () => {
  const [sessionDetails, setSessionDetails] = useState({
    date: "",
    coach: "",
  });

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("/api/create-practice", sessionDetails);
      alert.success("Practice session created successfully!");
    } catch (error) {
      console.error("Error creating practice session:", error);
      alert.error("An error occurred. Please try again later.");
    }
  };

  return (
    <div className="login-container">
      <h1>Create a New Practice Session</h1>
      <form onSubmit={handleSubmit}>
        <Input
          type="datetime-local"
          label="Date and Time"
          value={sessionDetails.date}
          onChange={(value) =>
            setSessionDetails({ ...sessionDetails, date: value })
          }
          required
        />
        <Input
          type="text"
          label="Coach"
          value={sessionDetails.coach}
          onChange={(value) =>
            setSessionDetails({ ...sessionDetails, coach: value })
          }
          required
        />
        <Button type="submit">Create Session</Button>
      </form>
    </div>
  );
};

export default CreatePractice;
