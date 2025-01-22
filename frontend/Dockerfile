# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN npm install

# Expose the port
EXPOSE 5173

# Command to run the application
CMD ["npm", "run", "dev"]
