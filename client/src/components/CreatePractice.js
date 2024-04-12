import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { AppContext } from "../index";
import { useNavigate, Link } from "react-router-dom";
import Input from "../reusable/Input";
import Button from "../reusable/Button";
import alert from "../lib/alert";

const CreatePractice = () => {
  const [name, setName] = useState("");
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");
  const [coach, setCoach] = useState("");
  const [price, setPrice] = useState("");
  const [coaches, setCoaches] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchCoaches = async () => {
    try {
      const response = await axios.get("/coaches", {
        headers: { Authorization: localStorage.getItem("token") },
      });
      setCoaches(response.data);
    } catch (err) {
      if (err.response.data.error) {
        alert(err.response.data.error, "error");
      }
    }
  };

  useEffect(() => {
    fetchCoaches();
  }, []);

  const renderCoaches = () => {
    return coaches.map((coach) => (
      <option key={coach.id} value={coach.id}>
        {coach.name}
      </option>
    ));
  };

  // Handle form submission
  const onFormSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const { data } = await axios.post(
        "/practice-create",
        {
          name,
          date,
          time,
          coach: coach,
          price,
        },
        {
          headers: { Authorization: localStorage.getItem("token") },
        }
      );
      // reset all the data
      setName("");
      setDate("");
      setTime("");
      setCoach("");
      setPrice("");
      setLoading(false);
      alert(data.message, "success");
    } catch (err) {
      if (err.response.data.error) {
        alert(err.response.data.error, "error");
      }
    }
  };

  return (
    <div className="new-session-container">
      <h1>New Practice Session Class</h1>
      <form onSubmit={onFormSubmit}>
        <div className="form-group">
          <Input
            required={true}
            type="text"
            label="Session Name"
            value={name}
            onChange={(value) => {
              setName(value);
            }}
          />
        </div>

        <div className="form-group u-margin-top-2">
          <Input
            required={true}
            type="number"
            label="Price"
            value={price}
            onChange={(value) => {
              setPrice(value);
            }}
          />
        </div>

        <div className="form-group">
          <label>Date</label>
          <input
            className="form-text__input"
            required={true}
            type="date"
            value={date}
            onChange={(event) => {
              setDate(event.target.value);
            }}
          />
        </div>

        <div className="form-group">
          <label>Time</label>
          <input
            className="form-text__input"
            required={true}
            type="time"
            value={time}
            onChange={(event) => {
              setTime(event.target.value);
            }}
          />
        </div>
        <div className="form-group">
          <label>Coach</label>
          <select
            className="form-text__input"
            required
            value={coach}
            onChange={(e) => {
              setCoach(e.target.value);
            }}
          >
            <option value="">-- Select a coach --</option>
            {renderCoaches()}
          </select>
        </div>

        <div className="form-group u-flex-text-right u-margin-top-2">
          <Button type="submit" color="blue" loading={loading}>
            Create
          </Button>
        </div>
      </form>
    </div>
  );
};

export default CreatePractice;
