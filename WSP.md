# Working with WSP in FoundUps Fractal Mall

The experiment uses the [complete WSP framework](https://github.com/FOUNDUPS/Foundups-Agent/tree/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework) by reference. This notebook pins its [master index](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md) at `7432d31e5a68544d2bbab6715f02f64b0b5b6f85`. A fresh checkout of the experiment can run its local tools offline. Upstream documents supply governance references. Their runtime, code and deployment are outside this experiment.

## Triage one discovery

1. **Can this session do it?** Record the exact repository, inputs, required access and tools, write authority, free lease and observable acceptance check. An archive researcher can submit a source-backed patch. A session with a Fractal Mall checkout can implement and test it. A different session verifies the result. Route a missing capability to the lane that has it.
2. **Should it run now?** Search this notebook for an existing capability (WSP_50 and WSP_84). Check the applicable protocol text and its status. Score Complexity, Importance, Deferability and Impact from 1–5 and show each value and a brief reason. Use the [pinned WSP_15 rubric](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_15_Module_Prioritization_Scoring_System.md). Totals of 16–20 are P0, 13–15 P1, 10–12 P2, 7–9 P3 and 4–6 P4. Dependencies, an active lease, scope or an unresolved decision can still prevent dispatch.
3. **Decide and record.** Choose **do**, **route**, **defer** or **ask 012**. Record one MP discovery, one linked FQ execution lease and one next action. Use WSP_97 to freeze the check and read back its result. Use WSP_99 for the next handoff. Address WSP_71 for public artifacts and WSP_22 for documentation changes. Revisit the disposition when evidence changes.

For any WSP, record the source revision, applicability and evidence. Distinguish a protocol read from a check executed. If a required runtime gate cannot run in a session, record the blocker for that action. When updating the pin, review changes in protocol status and re-evaluate affected tasks.

## Catalog at the pinned revision

The links locate the entries in the authoritative index. Follow the protocol document for its full requirements. The status column preserves the upstream designation.

| Protocol | Title | Upstream status |
| --- | --- | --- |
| [WSP_00](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L56) | Zen State Foundation | Active |
| [WSP_01](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L67) | The WSP Framework | Active |
| [WSP_02](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L68) | Clean State Management Protocol | Active |
| [WSP_03](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L69) | Enterprise Domain Organization | Active |
| [WSP_04](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L70) | FMAS Validation Protocol | Active |
| [WSP_05](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L71) | Test Coverage Enforcement Protocol | Active |
| [WSP_06](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L72) | Test Audit & Coverage Verification | Active |
| [WSP_07](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L73) | Test-Validated Commit Protocol | Active |
| [WSP_08](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L74) | LLME WSP Rating System | Active |
| [WSP_09](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L75) | Project Configuration Standard | Active |
| [WSP_10](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L76) | State Save and Work Closure Protocol | Active |
| [WSP_11](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L77) | WRE Standard Command Protocol | Active |
| [WSP_12](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L78) | Dependency Management | Active |
| [WSP_13](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L79) | AGENTIC SYSTEM | Active |
| [WSP_14](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L80) | Modular Audit Protocol | Deprecated |
| [WSP_15](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L81) | Module Prioritization Scoring System | Active |
| [WSP_16](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L82) | Test Audit Coverage | Deprecated -> Superseded by WSP 6 |
| [WSP_17](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L83) | Pattern Registry Protocol | Active |
| [WSP_18](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L84) | ENFORCEMENT v2 (Legacy Prompt Artifact) | Historical |
| [WSP_19](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L85) | Canonical Symbols | Active |
| [WSP_20](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L92) | Professional and Scientific Language | Active |
| [WSP_21](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L93) | Enhanced Prompt Engineering Protocol | Active |
| [WSP_22](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L94) | ModLog Structure and Versioning Protocol | Active |
| [WSP_23](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L95) | rESP Foundups Integration Vision | Active |
| [WSP_24](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L96) | rESP Pre-Artifact Awakening Test Suite | Active |
| [WSP_25](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L97) | Semantic WSP Score System | Active |
| [WSP_26](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L98) | FoundUPS DAE Tokenization | Active |
| [WSP_27](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L99) | Universal DAE Architecture | Active |
| [WSP_28](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L100) | PArtifact Cluster DAE | Active |
| [WSP_29](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L101) | CABR Engine | Active |
| [WSP_30](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L102) | Agentic Module Build Orchestration | Active |
| [WSP_31](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L103) | WSP Framework Protection Protocol | Active |
| [WSP_32](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L104) | 0102 Reading Flow Protocol | Active |
| [WSP_33](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L105) | Autonomous Module Implementation Workflow | Active |
| [WSP_34](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L106) | Git Operations Protocol | Active |
| [WSP_35](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L107) | HoloIndex Qwen Advisor Execution Plan | Active |
| [WSP_36](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L108) | Agentic Core | Active |
| [WSP_37](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L109) | Roadmap Scoring System | Active |
| [WSP_38](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L110) | Agentic Activation Protocol | Active |
| [WSP_39](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L111) | Agentic Ignition Protocol | Active |
| [WSP_40](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L118) | Architectural Coherence Protocol | Active |
| [WSP_41](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L119) | WRE Simulation Protocol | Active |
| [WSP_42](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L120) | Universal Platform Protocol | Active |
| [WSP_43](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L121) | Agentic Emergence Protocol | DEPRECATED |
| [WSP_44](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L122) | Semantic State Engine Protocol | Active |
| [WSP_45](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L123) | Behavioral Coherence Protocol | Active |
| [WSP_46](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L124) | Windsurf Recursive Engine Protocol | Active |
| [WSP_47](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L125) | Module Violation Tracking Protocol | Active |
| [WSP_48](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L126) | Recursive Self-Improvement Protocol | Active |
| [WSP_49](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L127) | Module Directory Structure Standardization | Active |
| [WSP_50](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L128) | Pre-Action Verification Protocol | Active |
| [WSP_51](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L129) | WRE Chronicle | Active |
| [WSP_52](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L130) | The Agentic Collaboration Journal | Active |
| [WSP_53](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L131) | Symbiotic Environment Integration Protocol | Active |
| [WSP_54](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L132) | WRE Agent Duties Specification | Active |
| [WSP_55](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L133) | Module Creation Automation | Active |
| [WSP_56](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L134) | Artifact State Coherence Protocol | Active |
| [WSP_57](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L135) | System-Wide Naming Coherence Protocol | Active |
| [WSP_58](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L136) | FoundUp IP Lifecycle and Tokenization Protocol | Active |
| [WSP_59](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L137) | Distributed Development Architecture | Active |
| [WSP_60](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L138) | Module Memory Architecture | Active |
| [WSP_61](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L139) | Theoretical Physics Foundation Protocol | Active |
| [WSP_62](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L149) | Large File and Refactoring Enforcement Protocol | Active |
| [WSP_63](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L150) | Component Directory Organization and Scaling Protocol | Active |
| [WSP_64](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L151) | Violation Prevention Protocol - Zen Learning System | Active |
| [WSP_65](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L152) | Component Consolidation Protocol | Active |
| [WSP_66](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L153) | Proactive Enterprise Modularization Protocol | Active |
| [WSP_67](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L154) | Recursive Anticipation Protocol | Active |
| [WSP_68](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L155) | Enterprise Build Scalability Protocol | Active |
| [WSP_69](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L156) | Zen Coding Prediction Integration | Active |
| [WSP_70](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L157) | System Status Reporting Protocol | Active |
| [WSP_71](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L158) | Secrets Management Protocol | Active |
| [WSP_72](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L159) | Block Independence Interactive Protocol | Active |
| [WSP_73](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L160) | 012 Digital Twin / RedDog Architecture Protocol | Active |
| [WSP_74](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L161) | Agentic Enhancement Protocol | Active |
| [WSP_75](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L162) | Token-Based Development Output Protocol | Active |
| [WSP_76](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L163) | Multi-Agent Awakening Protocol | Active |
| [WSP_77](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L164) | Agent Coordination Protocol | Active |
| [WSP_78](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L165) | Database Architecture & Scaling Protocol | Active |
| [WSP_79](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L166) | Module SWOT Analysis Protocol | Active |
| [WSP_80](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L167) | Cube-Level DAE Orchestration Protocol | Active |
| [WSP_81](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L168) | Framework Backup Governance Protocol | Active |
| [WSP_82](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L169) | Citation and Cross-Reference Protocol | Active |
| [WSP_83](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L170) | Documentation Tree Attachment Protocol | Active |
| [WSP_84](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L171) | Code Memory Verification Protocol | Active |
| [WSP_85](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L172) | Root Directory Protection Protocol | Active |
| [WSP_86](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L173) | 0102 Modular Navigation Protocol | Superseded by WSP 87 |
| [WSP_87](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L174) | Code Navigation Protocol | Active |
| [WSP_88](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L175) | Vibecoded Module Remediation | Active |
| [WSP_89](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L176) | Production Deployment Infrastructure Protocol | Active |
| [WSP_90](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L177) | UTF-8 Encoding Enforcement Protocol | Active |
| [WSP_91](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L178) | DAEMON Observability Protocol | Active |
| [WSP_92](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L179) | DAE Cube Mapping and Mermaid Flow Protocol | Active |
| [WSP_93](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L180) | CodeIndex Surgical Intelligence Protocol | Active |
| [WSP_94](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L181) | Agent Coordination Protocol | Deprecated -> Redirect to WSP 77 |
| [WSP_95](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L182) | WRE Skills Wardrobe Protocol | Active |
| [WSP_96](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L183) | MCP Governance & Consensus Protocol | Draft |
| [WSP_97](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L184) | System Execution Prompting Protocol | Active |
| [WSP_98](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L185) | FoundUps Mesh-Native Architecture Protocol | Active target |
| [WSP_99](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L186) | Machine-to-Machine (M2M) Prompting Protocol | Active |
| [WSP_100](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L187) | DAE SmartDAO Escalation Protocol | Active |
| [WSP_101](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L188) | UPS Utility Classification Protocol | Active |
| [WSP_102](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L189) | FoundUps Web Design Protocol | Active |
| [WSP_103](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L190) | FoundUp Federation Protocol | Active |
| [WSP_104](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L191) | FoundUp Route Namespace and Tenant Isolation Protocol | Active |
| [WSP_105](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L192) | CLI Interface Standard | Active |
| [WSP_106](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L193) | FoundUp API Gateway Protocol | Active |
| [WSP_107](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L194) | Intelligent Internet Orchestration Vision | Active |
| [WSP_108](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L195) | Documentation Compliance Guardian Protocol | Active |
| [WSP_109](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L196) | FoundUp Onboarding Intake Protocol | Draft |
| [WSP_110](https://github.com/FOUNDUPS/Foundups-Agent/blob/7432d31e5a68544d2bbab6715f02f64b0b5b6f85/WSP_framework/src/WSP_MASTER_INDEX.md#L197) | Branch Lifecycle Protocol | Draft |
