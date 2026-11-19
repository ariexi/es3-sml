# SML 4 Operational Sovereignty

*Operational sovereignty evaluates the capacity to run, maintain, and support services independently of external or unilateral provider controls.*

---

## Control Objectives & Controls

### SML 4.CO 1: Operational Control
**Target State:** To ensure operational control over the service is defined, transparent, and not solely dependent on the provider.

> **Sovereignty Contribution:** Ensures that operational control of the service is not exclusively held by the provider, enabling customers to retain influence over service operation and reducing operational dependency.

* **SML 4.CO 1.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts define operational roles and responsibilities, including allocation of control between the provider and customer.  
  * **Audit Question:** Does the contract clearly define operational roles, responsibilities, and the allocation of control between the provider and customer?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 4.CO 1.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Documented operational governance structures are implemented and maintained to clearly define responsibilities and control over service operation.  
  * **Audit Question:** Are there documented governance structures defining operational responsibilities and control over service operation?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 4.CO 1.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service provides customers with visibility and control over operational aspects relevant to their service usage.  
  * **Audit Question:** Can customers monitor and influence operational aspects of the service relevant to their usage?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 4.CO 1.C 4** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Critical operational actions cannot be executed solely by the provider without defined customer involvement or control where applicable.  
  * **Audit Question:** Are critical operational actions restricted such that they cannot be executed solely by the provider without defined customer involvement or control?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 4.CO 1.C 5** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *PaaS, IaaS*  
  The underlying services support operational control capabilities that enable separation of responsibilities and reduce dependency on a single provider for service operation.  
  * **Audit Question:** Do the underlying services support capabilities that enable separation of operational responsibilities and reduce dependency on a single provider?
  * **Maturity Levels:** `Future-Proof`

---

### SML 4.CO 2: Administrative Access
**Target State:** To ensure administrative access to the service is controlled and not exclusively held by the provider.

> **Sovereignty Contribution:** Ensures that administrative control over the service is not exclusively held by the provider, enabling customers to manage or influence privileged access and reducing dependency on provider-controlled administration.

* **SML 4.CO 2.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts define administrative roles, responsibilities, and privileged access, including allocation between the provider and customer.  
  * **Audit Question:** Does the contract clearly define administrative roles, responsibilities, and the allocation of privileged access between the provider and customer?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 4.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Policies and procedures are implemented and enforced to ensure administrative access is restricted, controlled, and assigned according to defined roles and responsibilities.  
  * **Audit Question:** Are there enforced policies and procedures ensuring that administrative access is restricted and assigned based on defined roles and responsibilities?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 4.CO 2.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service enables customers to manage and control administrative access rights where applicable.  
  * **Audit Question:** Can customers manage and control administrative access rights where applicable?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 4.CO 2.C 4** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Critical administrative actions cannot be executed solely by the provider without customer involvement, approval, or separation of duties.  
  * **Audit Question:** Are administrative actions restricted such that they cannot be executed solely by the provider without appropriate controls (e.g., customer approval or separation of duties)?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 4.CO 2.C 5** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Underlying services provide role-based administrative access control and separation of privileged access.  
  * **Audit Question:** Do the underlying services support role-based administrative access control and separation of privileged access?
  * **Maturity Levels:** `Future-Proof`

---

### SML 4.CO 3: Service Operations
**Target State:** To ensure service operations are defined, controlled, and do not create unmanaged dependency on the provider.

> **Sovereignty Contribution:** Ensures that day-to-day service operations are not solely controlled by the provider, enabling customers to retain influence over operational processes and reducing operational dependency.

* **SML 4.CO 3.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts define the scope, responsibilities, and allocation of day-to-day service operations between the provider and customer.  
  * **Audit Question:** Does the contract clearly define the scope, responsibilities, and allocation of day-to-day service operations between the provider and customer?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 4.CO 3.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Documented operational procedures are implemented and maintained to govern the execution of day-to-day service operations.  
  * **Audit Question:** Are documented operational procedures in place governing the execution of day-to-day service operations?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 4.CO 3.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service enables customers to monitor the operational status and execution of service operations relevant to their usage.  
  * **Audit Question:** Can customers monitor the operational status and execution of service operations relevant to their usage?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 4.CO 3.C 4** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Operational activities are executed according to defined procedures and cannot be performed in an uncontrolled or discretionary manner by the provider.  
  * **Audit Question:** Are service operations executed based on defined procedures without being subject to uncontrolled or discretionary execution by the provider?
  * **Maturity Levels:** `Future-Proof`

---

### SML 4.CO 4: Incident and Recovery
**Target State:** To ensure that incident response, recovery, and service continuity are defined, controlled, and not solely dependent on the provider.

> **Sovereignty Contribution:** Ensures that incident response and recovery are not exclusively controlled by the provider, enabling customers to retain influence over service restoration and continuity.

* **SML 4.CO 4.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts define incident response, recovery, and service continuity responsibilities, including allocation of roles between the provider and customer.  
  * **Audit Question:** Does the contract clearly define incident response, recovery, and service continuity responsibilities, including the allocation of roles between the provider and customer?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 4.CO 4.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Documented processes are implemented and maintained for incident response, recovery, and service continuity.  
  * **Audit Question:** Are documented processes in place governing incident response, recovery, and service continuity?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 4.CO 4.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service enables customers to monitor incidents and the status of recovery and continuity measures affecting their service usage.  
  * **Audit Question:** Can customers monitor incidents and the status of recovery and continuity measures affecting their service usage?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 4.CO 4.C 4** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Recovery and service restoration activities are executed according to defined procedures and do not rely solely on provider discretion.  
  * **Audit Question:** Are recovery and service restoration activities executed based on defined procedures and not solely dependent on provider discretion?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 4.CO 4.C 5** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service enables customers to influence or initiate recovery and data restoration processes where applicable.  
  * **Audit Question:** Can customers influence or initiate recovery and data restoration processes where applicable?
  * **Maturity Levels:** `Future-Proof`

* **SML 4.CO 4.C 6** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Underlying services provide backup, recovery, and failover capabilities to enable independent and controlled restoration of services and data.  
  * **Audit Question:** Do the underlying services provide backup, recovery, and failover capabilities that enable controlled and independent restoration of services and data?
  * **Maturity Levels:** `Future-Proof`

---

### SML 4.CO 5: Change and Service Evolution
**Target State:** To ensure that changes to the service are defined, controlled, and cannot be unilaterally executed by the provider.

> **Sovereignty Contribution:** Ensures that service changes are not exclusively controlled by the provider, enabling customers to retain influence over service evolution and preventing unilateral changes that impact service usage.

* **SML 4.CO 5.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts define change management responsibilities, including the roles of the provider and customer in approving and implementing service changes.  
  * **Audit Question:** Does the contract clearly define change management responsibilities, including the roles of the provider and customer in approving and implementing service changes?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 4.CO 5.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Documented change management processes are implemented and maintained to govern planning, approval, and implementation of service changes.  
  * **Audit Question:** Are documented change management processes in place governing the planning, approval, and implementation of service changes?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 4.CO 5.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service enables customers to be informed about and, where applicable, to approve or configure service changes affecting their usage.  
  * **Audit Question:** Are customers informed about service changes and, where applicable, able to approve or configure changes that impact their usage?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 4.CO 5.C 4** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  Changes affecting customer-relevant functionality or service behavior cannot be executed unilaterally by the provider without defined control mechanisms.  
  * **Audit Question:** Are changes affecting customer-relevant functionality or service behavior prevented from being executed unilaterally by the provider without defined control mechanisms?
  * **Maturity Levels:** `Future-Proof`

---
