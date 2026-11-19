# SML 9 - AI Sovereignty

*AI sovereignty evaluates the organizational oversight, system clarity, and independent control of artificial intelligence solutions.*

---

## Control Objectives & Controls

### SML 9.CO 1: AI Governance
**Target State:** To ensure that governance structures are established to define responsibility, oversight, and accountability for the development, deployment, and operation of AI systems.

> **Sovereignty Contribution:** Ensures that AI systems are subject to organizational oversight and are not operated without clear responsibility or control.

* **SML 9.CO 1.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  The service provider has defined and documented governance structures for the development, deployment, and operation of AI systems.  
  * **Audit Question:** Has the service provider defined and documented governance structures for the development, deployment, and operation of AI systems?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 9.CO 1.C 2** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *All*  
  The service ensures that AI-driven decisions can be controlled, restricted, or overridden where necessary.  
  * **Audit Question:** Does the service ensure that AI-driven decisions can be controlled, restricted, or overridden where necessary?
  * **Maturity Levels:** `Future-Proof`

* **SML 9.CO 1.C 3** | Level: *Governance & Operations* | Scope: *Client-Facing Service* | Service Type: *All*  
  The use of AI within the service can be configured or limited by the customer or operator.  
  * **Audit Question:** Can the use of AI within the service be configured or limited by the customer or operator?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 9.CO 2: AI Transparency
**Target State:** To achieve a situation whereby the provider ensures that the architecture, capabilities, limitations, and intended use of AI models are documented and communicated to relevant stakeholders.

> **Sovereignty Contribution:** Enables customers and regulators to understand how AI systems operate and prevents opaque “black box” dependencies.

* **SML 9.CO 2.C 1** | Level: *Governance & Operations* | Scope: *Client-Facing Service* | Service Type: *All*  
  The architecture, key components, capabilities, limitations, and intended use of AI models are defined and documented.  
  * **Audit Question:** Are the architecture, key components, capabilities, limitations, and intended use of AI models defined and documented?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 9.CO 2.C 2** | Level: *Governance & Operations* | Scope: *Client-Facing Service* | Service Type: *All*  
  AI documentation is made available to relevant stakeholders and customers in accordance with governance policies and legal requirements.  
  * **Audit Question:** Is documentation about AI systems available to relevant stakeholders?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 9.CO 3: Explainability
**Target State:** To ensure that AI systems are designed in a way that allows meaningful explanation of decision-making processes and enables human oversight or intervention where necessary.

> **Sovereignty Contribution:** Ensures that organizations remain in control of automated decision-making processes rather than delegating authority entirely to AI systems.

* **SML 9.CO 3.C 1** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *AI Service*  
  The service provides mechanisms to review AI-generated outputs or decisions before or after execution where relevant.  
  * **Audit Question:** Does the service provide mechanisms to review AI-generated outputs or decisions where relevant?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 9.CO 3.C 2** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *AI Service*  
  AI systems are designed to incorporate explainability mechanisms tailored to the underlying model type.  
  * **Audit Question:** Are AI systems designed to incorporate explainability mechanisms tailored to the underlying model type, including providing appropriate metrics and documentation?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 9.CO 3.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *AI Service*  
  Human oversight mechanisms are defined for critical AI-driven decisions.  
  * **Audit Question:** Are human oversight mechanisms defined for critical AI-driven decisions?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 9.CO 3.C 4** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  Policies and procedures define when and how human oversight is required for AI-driven decisions.  
  * **Audit Question:** Are policies and procedures defined specifying when and how human oversight is required for AI-driven decisions?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 9.CO 4: External AI Dependencies
**Target State:** To ensure that dependencies on external AI services are transparent, controlled, and do not lead to loss of control over AI functionality.

> **Sovereignty Contribution:** Prevents lock-in and loss of control by ensuring that reliance on external AI providers does not undermine autonomy or operational independence.

* **SML 9.CO 4.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  The service clearly identifies and documents dependencies on external AI services used within its functionality.  
  * **Audit Question:** Are dependencies on external AI services used within the service identified and documented?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 9.CO 4.C 2** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *All*  
  The service is designed to control or limit the use of external AI services where necessary.  
  * **Audit Question:** Is the service designed to control or limit the use of external AI services where necessary?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 9.CO 4.C 3** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Alternative solutions or fallback options are defined for critical dependencies on external AI services.  
  * **Audit Question:** Are alternative solutions or fallback options defined for critical dependencies on external AI services?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 9.CO 5: AI Life Cycle Management
**Target State:** To achieve a situation whereby the organization manages the life cycle of AI models, including training, validation, deployment, monitoring, retraining, and retirement.

> **Sovereignty Contribution:** Prevents uncontrolled model drift and ensures long-term accountability for AI behavior.

* **SML 9.CO 5.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  The life cycle of AI models is documented, including training, validation, deployment, monitoring, retirement and complete model lineage information.  
  * **Audit Question:** Is the life cycle of AI models documented and regularly reviewed?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 9.CO 5.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  AI models and changes are validated before deployment. Validation data is documentated and updated regularly.  
  * **Audit Question:** Are AI models validated before deployment and are validation procedures and results documented?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 9.CO 5.C 3** | Level: *Governance & Operations* | Scope: *Client-Facing Service* | Service Type: *AI Service*  
  AI model performance is regularly monitored after deployment.  
  * **Audit Question:** Are monitoring metrics defined and AI model performance monitored after deployment?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 9.CO 5.C 4** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  Processes exist for retraining or updating models when necessary.  
  * **Audit Question:** Are processes defined for retraining or updating AI models?
  * **Maturity Levels:** `Future-Proof`

---

### SML 9.CO 6: Control Over AI Assets
**Target State:** To ensure that AI model artifacts, including weights and architecture, remain under the control of the service provider and are protected from unauthorized access or modification by the infrastructure provider.

> **Sovereignty Contribution:** Preserves AI sovereignty by preventing infrastructure providers from accessing or modifying model artifacts during execution.

* **SML 9.CO 6.C 1** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *AI Service*  
  The service ensures that AI model artifacts (e.g., model weights, configurations) remain under the control of the service provider.  
  * **Audit Question:** Are AI model artifacts, including model weights, configurations, and architecture, documented and controlled by the service provider and protected from unauthorized access?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 9.CO 6.C 2** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *AI Service*  
  Access to AI model artifacts is restricted and controlled to prevent unauthorized access or modification.  
  * **Audit Question:** Is access to AI model artifacts restricted and controlled, including the documentation and enforcement of access permissions?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 9.CO 6.C 3** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *AI Service*  
  The service provider defines policies and processes to maintain control over AI model artifacts.  
  * **Audit Question:** Are policies and processes defined and implemented to maintain control over AI model artifacts?
  * **Maturity Levels:** `Advanced` `Future-Proof`

---

### SML 9.CO 7: External Access to Training Data
**Target State:** To ensure that dependencies on external AI providers do not allow access to training data, which must remain confidential and protected from disclosure, storage, or reuse by the external provider.

> **Sovereignty Contribution:** Preserves AI data sovereignty by preventing external AI providers from accessing or retaining training data during processing.

* **SML 9.CO 7.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Safeguards are defined and implemented to prevent disclosure or retention of training data.  
  * **Audit Question:** Are safeguards defined and implemented to prevent disclosure or retention of training data?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 9.CO 7.C 2** | Level: *Contractual* | Scope: *Service Provider* | Service Type: *All*  
  Contracts with external AI providers define restrictions on the use of customer data as training data.  
  * **Audit Question:** Do contracts with external AI providers restrict the use of customer data as training data?
  * **Maturity Levels:** `Advanced` `Future-Proof`

* **SML 9.CO 7.C 3** | Level: *Technical* | Scope: *Client-Facing Service* | Service Type: *All*  
  Technical mechanisms prevent external AI providers from storing or reusing training data.  
  * **Audit Question:** Are technical mechanisms implemented to prevent storage or reuse of training data by external providers?
  * **Maturity Levels:** `Future-Proof`

---

### SML 9.CO 8: Training Data
**Target State:** To achieve a situation whereby organizations maintain transparency and governance over the sources, ownership, and legal status of training data used for AI models.

> **Sovereignty Contribution:** Prevents hidden legal, ethical, or jurisdictional risks related to training datasets.

* **SML 9.CO 8.C 1** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Sources of training data used for AI models are documented, versioned, and periodically reviewed.  
  * **Audit Question:** Are sources of AI training data documented, versioned, and periodically reviewed?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

* **SML 9.CO 8.C 2** | Level: *Governance & Operations* | Scope: *Service Provider* | Service Type: *All*  
  Ownership and legal rights associated with training data for AI models are assessed and documented.  
  * **Audit Question:** Are ownership and legal rights associated with training data for AI models assessed and documented?
  * **Maturity Levels:** `Managed` `Advanced` `Future-Proof`

---
