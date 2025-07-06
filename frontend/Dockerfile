FROM node:20-alpine

WORKDIR /app

# --- add build tools required by node-gyp ---
RUN apk add --no-cache python3 make g++

# copy only the lock & manifest first to leverage layer-cache
COPY package*.json ./

# prefer deterministic installs
RUN npm ci                   
# or `npm install` if you don’t have a lock file

# now copy source
COPY . .

EXPOSE 3000
CMD ["npm", "run", "dev"]
