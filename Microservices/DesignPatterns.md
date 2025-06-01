# Design Patterns

[Tech-Interviews](../../README.md) -> [KnowledgeBase](../KnowledgeBase.md) -> [Microservices](../Microservices/Microservices.md) -> [Design Patterns](DesignPatterns.md)

𝐈𝐧𝐭𝐞𝐫𝐯𝐢𝐞𝐰𝐞𝐫 : What types of Microservices Design Patterns have you worked with?

𝐂𝐚𝐧𝐝𝐢𝐝𝐚𝐭𝐞:  Singleton, Factory, etc.

𝐈𝐧𝐭𝐞𝐫𝐯𝐢𝐞𝐰𝐞𝐫: Hold on, I’m asking about Microservices Design Patterns.

This is a common mistake I often notice among Java developers. Below is the information for those candidates who frequently struggle to answer this question.

𝐌𝐢𝐜𝐫𝐨𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬 𝐝𝐞𝐬𝐢𝐠𝐧 𝐩𝐚𝐭𝐭𝐞𝐫𝐧𝐬 𝐚𝐫𝐞 𝐞𝐬𝐬𝐞𝐧𝐭𝐢𝐚𝐥 𝐟𝐨𝐫 𝐛𝐮𝐢𝐥𝐝𝐢𝐧𝐠 𝐝𝐢𝐬𝐭𝐫𝐢𝐛𝐮𝐭𝐞𝐝 𝐬𝐲𝐬𝐭𝐞𝐦𝐬 𝐭𝐡𝐚𝐭 𝐚𝐫𝐞 𝐬𝐜𝐚𝐥𝐚𝐛𝐥𝐞, 𝐦𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐚𝐛𝐥𝐞, 𝐚𝐧𝐝 𝐟𝐥𝐞𝐱𝐢𝐛𝐥𝐞. 𝐁𝐞𝐥𝐨𝐰 𝐚𝐫𝐞 𝐬𝐨𝐦𝐞 𝐤𝐞𝐲 𝐝𝐞𝐬𝐢𝐠𝐧 𝐩𝐚𝐭𝐭𝐞𝐫𝐧𝐬 𝐮𝐬𝐞𝐝 𝐢𝐧 𝐦𝐢𝐜𝐫𝐨𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬 𝐚𝐫𝐜𝐡𝐢𝐭𝐞𝐜𝐭𝐮𝐫𝐞:

1. 𝑫𝒆𝒄𝒐𝒎𝒑𝒐𝒔𝒊𝒕𝒊𝒐𝒏 𝑷𝒂𝒕𝒕𝒆𝒓𝒏𝒔: 
𝘚𝘦𝘳𝘷𝘪𝘤𝘦 𝘱𝘦𝘳 𝘍𝘶𝘯𝘤𝘵𝘪𝘰𝘯𝘢𝘭𝘪𝘵𝘺: Each microservice is designed to handle a specific functionality or business capability.

𝘋𝘢𝘵𝘢𝘣𝘢𝘴𝘦 𝘱𝘦𝘳 𝘚𝘦𝘳𝘷𝘪𝘤𝘦 : Each service manages its own database, ensuring loose coupling between services.

2. 𝑫𝒂𝒕𝒂 𝑴𝒂𝒏𝒂𝒈𝒆𝒎𝒆𝒏𝒕 𝑷𝒂𝒕𝒕𝒆𝒓𝒏𝒔
𝘚𝘢𝘨𝘢 𝘗𝘢𝘵𝘵𝘦𝘳𝘯 : Used to manage distributed transactions across multiple services. It helps maintain data consistency in distributed environments.

𝘊𝘘𝘙𝘚 (𝘊𝘰𝘮𝘮𝘢𝘯𝘥 𝘘𝘶𝘦𝘳𝘺 𝘙𝘦𝘴𝘱𝘰𝘯𝘴𝘪𝘣𝘪𝘭𝘪𝘵𝘺 𝘚𝘦𝘨𝘳𝘦𝘨𝘢𝘵𝘪𝘰𝘯) :This pattern separates read and write operations to handle data more efficiently in different use cases.

𝘌𝘷𝘦𝘯𝘵 𝘚𝘰𝘶𝘳𝘤𝘪𝘯𝘨 :Instead of directly updating a database, changes are captured as a series of events, making it easier to trace and revert actions.

3. 𝑪𝒐𝒎𝒎𝒖𝒏𝒊𝒄𝒂𝒕𝒊𝒐𝒏 𝑷𝒂𝒕𝒕𝒆𝒓𝒏𝒔
𝘈𝘗𝘐 𝘎𝘢𝘵𝘦𝘸𝘢𝘺 :A single entry point that handles requests, routes them to the appropriate microservices, and aggregates the responses if needed.

𝘚𝘦𝘳𝘷𝘪𝘤𝘦 𝘋𝘪𝘴𝘤𝘰𝘷𝘦𝘳𝘺: Services dynamically discover each other through a registry like Consul or Eureka, eliminating hardcoded network addresses.

𝘊𝘪𝘳𝘤𝘶𝘪𝘵 𝘉𝘳𝘦𝘢𝘬𝘦𝘳: Prevents cascading failures by monitoring service interactions and breaking the circuit if a service is failing.

𝘔𝘦𝘴𝘴𝘢𝘨𝘦 𝘉𝘳𝘰𝘬𝘦𝘳: Asynchronous messaging systems (like RabbitMQ, Kafka) that decouple communication between microservices.

4. 𝑶𝒃𝒔𝒆𝒓𝒗𝒂𝒃𝒊𝒍𝒊𝒕𝒚 𝑷𝒂𝒕𝒕𝒆𝒓𝒏𝒔
𝘓𝘰𝘨 𝘈𝘨𝘨𝘳𝘦𝘨𝘢𝘵𝘪𝘰𝘯: Collects logs from different services into a centralized logging system for easier debugging.

𝘋𝘪𝘴𝘵𝘳𝘪𝘣𝘶𝘵𝘦𝘥 𝘛𝘳𝘢𝘤𝘪𝘯𝘨:Traces requests across microservices to identify performance bottlenecks and pinpoint failures.

5. 𝑺𝒆𝒄𝒖𝒓𝒊𝒕𝒚 𝑷𝒂𝒕𝒕𝒆𝒓𝒏𝒔
𝘛𝘰𝘬𝘦𝘯-𝘉𝘢𝘴𝘦𝘥 𝘈𝘶𝘵𝘩𝘦𝘯𝘵𝘪𝘤𝘢𝘵𝘪𝘰𝘯: Uses OAuth, JWT for securing communication between microservices.

𝘚𝘦𝘳𝘷𝘪𝘤𝘦 𝘔𝘦𝘴𝘩:A dedicated infrastructure layer that provides security, routing, and monitoring between services .Example : Istio, Linkerd