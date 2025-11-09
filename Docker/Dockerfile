# use official nodejs image as base
FROM node:18

# set working directory inside the container
WORKDIR /app

# install dependencies
# RUN npm install

# copy all remaining source files
COPY . .

# directly run docker you js file
CMD ["node", "index.js"]
