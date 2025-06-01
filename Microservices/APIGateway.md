# API Gateway

[Tech-Interviews](../../README.md) -> [KnowledgeBase](../KnowledgeBase.md) -> [Microservices](../Microservices/Microservices.md) -> [API Gateway](APIGateway.md)

API Gateway - System Design Pattern

Microservices are used to break big applications into smaller, more manageable parts. Handling communication between clients and different microservices can be difficult. That's where an API Gateway comes in.

𝐇𝐨𝐰 𝐚𝐧 𝐀𝐏𝐈 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 𝐖𝐨𝐫𝐤𝐬
An API Gateway acts as a middleman between the client and the microservices. It takes care of all requests from the client and sends them to the correct microservice. The gateway works like a reverse proxy, giving the client a single point to interact with.

𝐇𝐨𝐰 𝐢𝐭 𝐖𝐨𝐫𝐤𝐬:
1. Client Request: Instead of contacting each microservice separately, the client sends one request to the API Gateway.
2. Routing: The API Gateway sends the request to the right service.
3. Load Balancing & Caching: The Gateway manages traffic by balancing the load and caching responses to improve speed.
4. Security: It handles authentication (who can access) and authorization (what they can access).
5. Aggregating Responses: If the request needs data from multiple services, the Gateway collects the results and sends one response back to the client.

This makes the process more efficient, reduces delays, and simplifies the client's work by sending one request for all the services.

𝐁𝐞𝐧𝐞𝐟𝐢𝐭𝐬 𝐨𝐟 𝐔𝐬𝐢𝐧𝐠 𝐚𝐧 𝐀𝐏𝐈 𝐆𝐚𝐭𝐞𝐰𝐚𝐲:
1. Simplified Communication: Clients only need to send one request, and the gateway handles the rest.
2. Centralized Security: Authentication and authorization are done in one place, so each microservice doesn’t need to handle it individually.
3. Load Balancing: The gateway manages the traffic efficiently, improving the performance of the system.
4. Faster Updates: Microservices can be updated or changed without affecting how the client interacts with the system.
5. Decoupled Architecture: The client doesn’t need to know how the services are structured, making internal changes easier.
6. Support for Multiple Protocols: API Gateways can work with different communication methods like REST, gRPC, and WebSockets.

𝐈𝐧𝐭𝐞𝐫𝐯𝐢𝐞𝐰 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬:
1. What is an API Gateway, and why is it used in microservices?
2. What problems can arise in client-to-microservice communication, and how does an API Gateway solve them?
3. How does load balancing work in an API Gateway?
4. What’s the difference between an API Gateway and a Backend for Frontend (BFF)?
5. How does an API Gateway help with security in microservices?
6. What are some disadvantages of using an API Gateway?
7. How does an API Gateway improve performance using caching?
8. Can you name some popular API Gateway tools? How are they different?
9. What is a service mesh, and how is it different from an API Gateway?
10. What is API composition or aggregation, and when is it useful?