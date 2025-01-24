export const fetchUsers = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/users");
      return await response.json();
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };
  