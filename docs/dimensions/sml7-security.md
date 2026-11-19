# SML 7 Security and Compliance Sovereignty

*Security and compliance sovereignty evaluates the isolation, administrative control, and auditability of security configurations and compliance mechanisms.*

---

## Control Objectives & Controls

### SML 7.CO 1: Identity and Access
**Target State:** To ensure that access to the service is protected and controlled to prevent unauthorized use.

> **Sovereignty Contribution:** Ensures that access to the service is securely controlled and not solely dependent on the provider, enabling customers to retain control over identities and access permissions.

* **SML 7.CO 1.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Policies for identity and access, including authentication, authorization, and access control, are formally defined and documented.  
  * **Audit Question:** Are policies defined and maintained for identity and access management, including authentication, authorization, and access control principles?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 7.CO 1.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Privileged access is restricted, documented, monitored, and managed according to defined controls.  
  * **Audit Question:** Is access to privileged accounts limited, documented, and regularly monitored for compliance with defined controls?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 7.CO 1.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Strong authentication mechanisms, including multi-factor authentication for privileged or sensitive access, are enforced for all user accounts.  
  * **Audit Question:** Are strong authentication mechanisms enforced in accordance with defined policies, including multi-factor authentication for privileged or sensitive access?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 7.CO 1.C 4** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Access is controlled using role-based or attribute-based mechanisms, ensuring users only have access according to their defined roles and responsibilities.  
  * **Audit Question:** Is there a formal concept or policy for role-based or attribute-based access controls that ensures users have access only according to their defined roles and responsibilities?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 7.CO 1.C 5** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Segregation of access between the customer and provider is enforced, preventing unauthorized or undisclosed privileged access by the provider.  
  * **Audit Question:** How is access between the customer and provider controlled to prevent unrestricted or undisclosed privileged access by the provider?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 7.CO 1.C 6** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *PaaS, IaaS*  
  Identity and access control mechanisms, including identity federation and integration with external identity providers, are supported and enforced for all users.  
  * **Audit Question:** How are identity and access control mechanisms implemented in the underlying services, including identity federation and integration with external identity providers?
  * **Maturity Levels:** `Future-Proof`

---

### SML 7.CO 2: Security Visibility and Control
**Target State:** To ensure that customers have visibility into and control over security mechanisms relevant to their service.

> **Sovereignty Contribution:** Ensures that customers are not dependent on the provider’s internal security operations by providing visibility and control over relevant security mechanisms.

* **SML 7.CO 2.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Documented policies are in place for providing customers with visibility into and control over security mechanisms, and mechanisms are in place to enforce the implementation of these policies.  
  * **Audit Question:** Are policies defined and maintained to provide customers with visibility into and control over security mechanisms?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 7.CO 2.C 2** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Customers are provided with role-based access to view security configurations and settings relevant to their service usage.  
  * **Audit Question:** Are mechanisms in place to provide customers with role-based access to view security configurations and mechanisms relevant to their service usage?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 7.CO 2.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Authorized customer users can configure and manage security settings within their scope of responsibility through defined interfaces.  
  * **Audit Question:** Are mechanisms in place that enable authorized customer users to configure and manage security settings within their defined scope of responsibility through defined interfaces?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 7.CO 2.C 4** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *PaaS, IaaS*  
  Customers have visibility into security-relevant configurations and their impact on the service, including logging of configuration changes.  
  * **Audit Question:** Are mechanisms in place to provide customers with visibility into security-relevant configurations and their impact on the service, including logging of configuration changes?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 7.CO 2.C 5** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *PaaS, IaaS*  
  Underlying services allow configuration and management of security controls, ensuring that configurations are valid and secure.  
  * **Audit Question:** Do the underlying services provide mechanisms to configure and manage security controls relevant to the service, ensuring configurations are valid and secure?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 7.CO 3: Sensitive Operations
**Target State:** To ensure that sensitive operations are protected against misuse or unauthorized execution.

> **Sovereignty Contribution:** Ensures that critical operations cannot be executed without appropriate protection, reducing the risk of misuse and strengthening customer control over high-impact actions.

* **SML 7.CO 3.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Documented policies are in place for protecting sensitive operations against misuse or unauthorized execution, and mechanisms are in place to enforce these policies.  
  * **Audit Question:** Are policies defined and maintained to protect sensitive operations against misuse or unauthorized execution?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 7.CO 3.C 2** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Additional safeguards for sensitive operations, such as multistep approval, strong authentication, or confirmation mechanisms, are implemented and enforced.  
  * **Audit Question:** Are additional safeguards enforced for sensitive operations, such as multistep approval, strong authentication, or confirmation mechanisms?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 7.CO 3.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Execution of sensitive operations is restricted to authorized roles with clearly defined permissions.  
  * **Audit Question:** Are sensitive operations restricted to authorized roles with clearly defined permissions?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 7.CO 3.C 4** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Mechanisms are in place to log and ensure traceability of sensitive operations.  
  * **Audit Question:** Are sensitive operations traceable and logged?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 7.CO 3.C 5** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *PaaS, IaaS*  
  Underlying services protect and control the execution of sensitive operations, enforcing defined security requirements.  
  * **Audit Question:** Do the underlying services support mechanisms to protect and control the execution of sensitive operations, including enforcement of defined security requirements?
  * **Maturity Levels:** `Future-Proof`

---
