# SML 6 - Technology Sovereignty

*Technology sovereignty assesses the openness, auditability, and physical or logical layout of the underlying technical stack.*

---

## Control Objectives & Controls

### SML 6.CO 1: Infrastructure Location and Control
**Target State:** To ensure that the physical and virtual infrastructure is located and controlled within approved jurisdictions.

> **Sovereignty Contribution:** Ensures that the infrastructure underpinning the service is located and controlled within approved jurisdictions, preventing exposure to non-approved legal environments and reducing sovereignty risks.

* **SML 6.CO 1.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts are in place to ensure that all infrastructure used to deliver the service is located within jurisdictions listed in the AJL.  
  * **Audit Question:** Does the contract ensure that all infrastructure used to deliver the service is located within approved jurisdictions?
  * **Maturity Levels:** `Initial` `Managed` `Advanced` `Future-Proof`

* **SML 6.CO 1.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Documented policies exist governing the selection and use of infrastructure locations, ensuring alignment with jurisdictions listed in the AJL.  
  * **Audit Question:** Are policies in place governing the selection and use of infrastructure locations to ensure alignment with approved jurisdictions?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 6.CO 1.C 3** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *PaaS, IaaS*  
  All infrastructure components, including primary, backup, failover, and replication environments, are located within jurisdictions listed in the AJL.  
  * **Audit Question:** Are all infrastructure components, including primary, backup, failover, and replication environments, located within approved jurisdictions?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 6.CO 1.C 4** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *PaaS, IaaS*  
  Transfers or processing of workloads to/via infrastructure not located within approved jurisdictions are prevented, including during failover or scaling scenarios.  
  * **Audit Question:** Are mechanisms in place to prevent workloads from being transferred to or processed via infrastructure not located within approved jurisdictions, including during failover or scaling scenarios?
  * **Maturity Levels:** `Future-Proof`

* **SML 6.CO 1.C 5** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service provides visibility into the locations of infrastructure used to deliver the service, including primary and secondary environments.  
  * **Audit Question:** Are customers provided with visibility into the locations of infrastructure used to deliver the service, including primary and secondary environments?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 6.CO 2: Use of Open Standards
**Target State:** To ensure that open standards and interoperable technologies are used where feasible.

> **Sovereignty Contribution:** Enables customers to identify technological dependencies and assess sovereignty risks related to external platforms, third-party components, and jurisdictional exposure.

* **SML 6.CO 2.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Documented guidelines exist for using open standards and interoperable technologies in service design and implementation.  
  * **Audit Question:** Are guidelines defined and maintained for the use of open standards and interoperable technologies in service design and implementation?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 6.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  The use of proprietary versus open standards is assessed and documented, including justification for any proprietary technologies.  
  * **Audit Question:** Is the use of proprietary versus open standards assessed and documented, including justification for any proprietary technologies used?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 6.CO 2.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service implements interfaces, data formats, and protocols based on open standards to enable interoperability where feasible.  
  * **Audit Question:** Are service interfaces, data formats, and protocols implemented using open standards to ensure interoperability where feasible?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 6.CO 2.C 4** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *IaaS, PaaS*  
  Underlying services use open and standardized technologies to enable interoperability and avoid enforced reliance on proprietary mechanisms.  
  * **Audit Question:** Do the underlying services support the use of open and standardized technologies, enabling interoperability and avoiding enforced use of proprietary mechanisms?
  * **Maturity Levels:** `Future-Proof`

* **SML 6.CO 2.C 5** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service avoids reliance on proprietary interfaces or formats that would limit interoperability or substitution.  
  * **Audit Question:** Does the service use system architecture and technical specifications to avoid reliance on proprietary interfaces or formats where such reliance would limit interoperability or substitution?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 6.CO 3: Portability and Interoperability
**Target State:** To enable the service to be ported and integrated across different technical environments.

> **Sovereignty Contribution:** Ensures that the service can be migrated and integrated across different environments, reducing technical barriers and enabling flexibility and independence.

* **SML 6.CO 3.C 1** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Documented guidelines exist for designing services to enable portability and interoperability across different technical environments.  
  * **Audit Question:** Are guidelines defined and maintained for designing services to ensure portability and interoperability across different technical environments?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 6.CO 3.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Portability assessments are conducted and documented, including the effort, constraints, and dependencies involved in migration to alternative environments.  
  * **Audit Question:** Is the portability of the service assessed and documented, including the required effort, constraints, and dependencies involved in migration to alternative environments?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 6.CO 3.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service is designed and implemented using portable technologies and deployment models to enable deployment and operation across multiple environments.  
  * **Audit Question:** Is the service designed and implemented to support deployment and operation across multiple environments using portable technologies and deployment models where feasible?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 6.CO 3.C 4** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *Managed Service, AI Service, SaaS*  
  The service provides standardized and interoperable interfaces to enable integration with external systems.  
  * **Audit Question:** Does the service support integration with external systems through standardized and interoperable interfaces?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 6.CO 3.C 5** | Level: *Technical* | Scope: *Underlying Service* | Service Type: *PaaS, IaaS*  
  Underlying services are configured to allow deployment, migration, and operation of workloads across different environments without enforcing platform-specific constraints.  
  * **Audit Question:** Do the underlying services support deployment, migration, and operation of workloads across different environments without enforcing platform-specific constraints?
  * **Maturity Levels:** `Future-Proof`

---

### SML 6.CO 4: Technology Control and Transparency
**Target State:** To ensure that the technology stack is transparent and under defined control.

> **Sovereignty Contribution:** Ensures that the technology stack is fully transparent and governed, enabling control over technical components and preventing hidden dependencies or opaque architectures.

* **SML 6.CO 4.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  The service provides customers with visibility into technology stack components that affect their service usage.  
  * **Audit Question:** Is a complete and up-to-date inventory of the technology stack maintained, including platforms, components, and dependencies used to deliver the service?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 6.CO 4.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Governance processes exist for approving, managing, and controlling changes to the technology stack.  
  * **Audit Question:** Are governance processes in place for approving, managing, and controlling changes to the technology stack?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 6.CO 4.C 3** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  All components used in the technology stack are disclosed, managed, and controlled to prevent hidden dependencies or risks.  
  * **Audit Question:** Are mechanisms in place to ensure that no undisclosed or unmanaged components are used within the technology stack?
  * **Maturity Levels:** `Future-Proof`

---
