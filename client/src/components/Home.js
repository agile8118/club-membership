import React, { useState, useEffect, useContext } from "react";
import { AppContext } from "../index";
import axios from "axios";
import InlineLoading from "../reusable/InlineLoading";

const Home = () => {
  const { loggedIn } = useContext(AppContext);
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    console.log("HEY");
    fetchUserData();
  }, [loggedIn]);

  const fetchUserData = async () => {
    try {
      setLoading(true);
      const response = await axios.get("/user", {
        headers: { Authorization: localStorage.getItem("token") },
      });
      setUserData(response.data);
    } catch (error) {
      setUserData(null);
    }
    setLoading(false);
  };

  if (loading) {
    return (
      <div className="u-text-center u-margin-top-3">
        <InlineLoading color="gray" />
      </div>
    );
  }

  return (
    <div className="home-message">
      {!userData && (
        <h1>
          Welcome to the Club Membership App, login to access our features!
        </h1>
      )}

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
        <div>
          We still haven't added any features for our coaches on the website,
          stay tuned!
        </div>
      )}
    </div>
  );
};

export default Home;
