import React, { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import { verifyOtp } from "../services/authService";

const VerifyOtp = () => {
  const [otp, setOtp] = useState("");
  const navigate = useNavigate();
  const location = useLocation();
  const phone = location.state?.phone;

  const handleVerify = async (e) => {
    e.preventDefault();
    try {
      const data = await verifyOtp(phone, otp);
      if (data.new_user) {
        navigate("/register", { state: { phone } });
      } else if (data.tokens && data.user) {
        localStorage.setItem("tokens", JSON.stringify(data.tokens));
        localStorage.setItem("user", JSON.stringify(data.user));
        navigate("/");
      } else {
        throw new Error("Invalid response from server");
      }
    } catch (error) {
      alert(error.message);
    }
  };

  return (
    <div style={styles.container}>
      <h2>Verify OTP</h2>
      <form onSubmit={handleVerify} style={styles.form}>
        <input
          type="text"
          placeholder="Enter OTP"
          value={otp}
          onChange={(e) => setOtp(e.target.value)}
          required
          style={styles.input}
        />
        <button type="submit" style={styles.button}>
          Verify
        </button>
      </form>
    </div>
  );
};

const styles = {
  container: { display: "flex", flexDirection: "column", alignItems: "center", marginTop: "50px" },
  form: { display: "flex", flexDirection: "column", gap: "10px", width: "200px" },
  input: { padding: "10px", fontSize: "16px" },
  button: { padding: "10px", background: "#007bff", color: "white", border: "none", cursor: "pointer" },
};

export default VerifyOtp;