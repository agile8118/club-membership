import React, { useState, useEffect, useContext } from "react";
import axios from "axios";

const Home = () => {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    fetchUserData();
  }, []);

  const fetchUserData = async () => {
    try {
      const response = await axios.get("/user", {
        headers: { Authorization: localStorage.getItem("token") },
      });
      setUserData(response.data);
    } catch (error) {
      console.error("Error fetching user data:", error);
    }
  };

  return (
    <div className="home-message">
      {userData && (
        <h1>Welcome to the Club Membership App, {userData.name}!</h1>
      )}

      {userData && userData.role === "member" && (
        <div>
          As a regular member, you can check out and sign up for our practice
          session classes!
        </div>
      )}

      {userData && userData.role === "treasurer" && (
        <div>
          As a treasurer, you can schedule new practice session classes!
        </div>
      )}

      {userData && userData.role === "coach" && (
        <div>As a coach, you can see the practice session assigned to you!</div>
      )}
    </div>
  );
};

export default Home;
