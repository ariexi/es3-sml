# SML 5 Supply Chain Sovereignty

*Supply chain sovereignty measures the geographic composition, component tracking, and systemic resilience of the third-party ecosystem supporting the service.*

---

## Control Objectives & Controls

### SML 5.CO 1: Transparency
**Target State:** To ensure dependencies on third-party providers are identified and transparent.

> **Sovereignty Contribution:** Ensures that customers have visibility into all third-party dependencies, enabling informed decisions and reducing hidden supply chain risks.

* **SML 5.CO 1.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts with third-party providers disclose their involvement, roles, and responsibilities in delivering the service.  
  * **Audit Question:** Does the contract disclose all third-party providers involved in delivering the service, including their roles and responsibilities?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 5.CO 1.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  An inventory of third-party dependencies, including subservice providers and external integrations, is maintained and documented.  
  * **Audit Question:** Is there a maintained and documented inventory of all third-party dependencies, including subservice providers and external integrations?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 5.CO 1.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service provides customers with visibility into third-party dependencies that impact their service usage.  
  * **Audit Question:** Are customers provided with visibility into third-party dependencies that impact their service usage?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 5.CO 2: Supplier Governance
**Target State:** To ensure that third-party providers are governed and controlled to prevent unmanaged dependency.

> **Sovereignty Contribution:** Ensures that third-party providers are subject to defined governance and control mechanisms, reducing dependency risks and preventing uncontrolled external influence on the service.

* **SML 5.CO 2.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts with third-party providers define governance, roles, responsibilities, and control mechanisms for service delivery.  
  * **Audit Question:** Does the contract define governance, responsibilities, and control mechanisms for third-party providers involved in service delivery?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 5.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Governance processes are implemented and maintained to manage third-party providers, including oversight, performance monitoring, and risk management.  
  * **Audit Question:** Are governance processes in place for managing third-party providers, including oversight, performance monitoring, and risk management?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 5.CO 2.C 3** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Third-party providers are integrated into service governance structures and subject to defined controls and oversight.  
  * **Audit Question:** Are third-party providers integrated into service governance structures and subject to defined control and oversight mechanisms?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 5.CO 3: Dependency Management
**Target State:** To ensure that critical dependencies are identified and managed to reduce risk and dependency.

> **Sovereignty Contribution:** Ensures that critical dependencies are identified and actively managed, reducing concentration risk and preventing excessive reliance on individual third-party providers.

* **SML 5.CO 3.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Criteria are defined to identify and classify critical third-party dependencies based on their impact on service delivery, data, and operations.  
  * **Audit Question:** Are criteria defined to identify and classify critical third-party dependencies based on their impact on service delivery, data, and operations?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 5.CO 3.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Documented assessments are performed and maintained to determine the criticality and associated risks of third-party dependencies.  
  * **Audit Question:** Are documented assessments performed and maintained to determine the criticality and associated risks of third-party dependencies?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 5.CO 3.C 3** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Measures are implemented and maintained to manage and mitigate risks associated with critical third-party dependencies.  
  * **Audit Question:** Are measures implemented and maintained to manage and mitigate risks associated with critical dependencies?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 5.CO 4: Substitution and Exit
**Target State:** To ensure that dependencies can be substituted or exited without excessive disruption.

> **Sovereignty Contribution:** Ensures that dependencies are structured to allow underlying providers to be replaced or relationships with them to be exited, reducing vendor lock-in and enabling continuity of service without excessive disruption.

* **SML 5.CO 4.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Exit strategies are defined and maintained for third-party dependencies, including procedures to replace or terminate providers.  
  * **Audit Question:** Are exit strategies defined and maintained for third-party dependencies, including procedures for replacing or terminating providers?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 5.CO 4.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  The feasibility, impact, and effort involved in substituting providers or exiting relationships with them are assessed and documented for critical third-party dependencies.  
  * **Audit Question:** Are the feasibility, impact, and effort required to substitute providers or exit relationships with them assessed and documented for critical third-party dependencies?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 5.CO 4.C 3** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Processes are in place for the substitution of providers or the exit of relationships with them without causing unacceptable disruption to service delivery in the context of third-party dependencies.  
  * **Audit Question:** Can providers be substituted or relationships with them be exited without causing unacceptable disruption to service delivery in the context of third-party dependencies?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 5.CO 4.C 4** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *All*  
  The service architecture is designed to minimize dependency on single third-party providers and supports substitution where feasible.  
  * **Audit Question:** Is the service architecture designed to reduce dependency on single third-party providers and support substitution where feasible?
  * **Maturity Levels:** `Future-Proof`

---

### SML 5.CO 5: Requirement flow-down
**Target State:** To ensure that digital sovereignty and control requirements are enforced across the supply chain.

> **Sovereignty Contribution:** Ensures that sovereignty and control requirements are consistently enforced across all third-party providers, preventing gaps and reducing risk from weak links in the supply chain.

* **SML 5.CO 5.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts with third-party providers require compliance with defined digital sovereignty and control requirements.  
  * **Audit Question:** Do contracts with third-party providers ensure that sovereignty and control requirements are imposed on them?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 5.CO 5.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Processes are implemented and maintained to verify that third-party providers comply with defined digital sovereignty and control requirements.  
  * **Audit Question:** Are processes in place to verify that third-party providers comply with defined sovereignty and control requirements?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 5.CO 5.C 3** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Non-compliance by third-party providers is identified, managed, and remediated through defined processes.  
  * **Audit Question:** Is non-compliance by third-party providers identified, managed, and remediated in a controlled manner?
  * **Maturity Levels:** `Future-Proof`

---
