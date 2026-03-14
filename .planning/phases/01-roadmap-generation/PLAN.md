---
phase: 01-roadmap-generation
plan: 01
type: execute
wave: 1
depends_on: []
files_modified: []
autonomous: true
requirements: [TEST-RM]

must_haves:
  truths:
    - "ROADMAP.md follows the GSD schema with all required sections"
    - "STATE.md reflects Phase 1 as the current project status"
    - "REQUIREMENTS.md correctly maps TEST-RM to Phase 1 in the traceability table"
  artifacts:
    - path: ".planning/ROADMAP.md"
      provides: "Project roadmap and phase definitions"
    - path: ".planning/STATE.md"
      provides: "Current project state tracking"
    - path: ".planning/REQUIREMENTS.md"
      provides: "Requirement definitions and traceability"
  key_links:
    - from: ".planning/ROADMAP.md"
      to: ".planning/REQUIREMENTS.md"
      via: "Requirement IDs (e.g., TEST-RM)"
---

<objective>
Verify that the initial roadmap artifacts generated for the Test Project are correctly formatted, internally consistent, and properly integrated according to GSD standards.

Purpose: Ensure the foundation for agent verification is solid before proceeding to planning and execution phases.
Output: Verification of ROADMAP.md, STATE.md, and REQUIREMENTS.md.
</objective>

<execution_context>
@/home/arika/.gemini/get-shit-done/workflows/execute-plan.md
@/home/arika/.gemini/get-shit-done/templates/summary.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
@.planning/STATE.md
@.planning/REQUIREMENTS.md
</context>

<tasks>

<task type="auto">
  <name>Task 1: Verify ROADMAP.md structure and consistency</name>
  <files>.planning/ROADMAP.md</files>
  <action>
    Inspect `.planning/ROADMAP.md` to ensure it contains the following mandatory sections:
    - ## Overview
    - ## Phases
    - ## Phase Details
    - ## Progress

    Verify that Phase 1's goal matches the intent of verifying roadmap generation and that it correctly references the requirement `TEST-RM`.
  </action>
  <verify>
    <automated>grep -E "## (Overview|Phases|Phase Details|Progress)" .planning/ROADMAP.md && grep "TEST-RM" .planning/ROADMAP.md</automated>
  </verify>
  <done>ROADMAP.md is valid, contains all required sections, and correctly references requirements.</done>
</task>

<task type="auto">
  <name>Task 2: Verify STATE.md project position</name>
  <files>.planning/STATE.md</files>
  <action>
    Inspect `.planning/STATE.md` to ensure it contains:
    - ## Current Phase
    - ## Summary
    - ## Recent Activity
    - ## Next Actions

    Confirm that "Current Phase" is explicitly set to "Phase 1: Roadmap Generation".
  </action>
  <verify>
    <automated>grep "## Current Phase" .planning/STATE.md -A 1 | grep "Phase 1: Roadmap Generation"</automated>
  </verify>
  <done>STATE.md is valid and correctly identifies the current phase.</done>
</task>

<task type="auto">
  <name>Task 3: Verify REQUIREMENTS.md traceability</name>
  <files>.planning/REQUIREMENTS.md</files>
  <action>
    Inspect the "Traceability" section of `.planning/REQUIREMENTS.md`. 
    Verify that the requirement `TEST-RM` is mapped to `Phase 1`.
  </action>
  <verify>
    <automated>grep "TEST-RM" .planning/REQUIREMENTS.md | grep "Phase 1"</automated>
  </verify>
  <done>Traceability mapping for Phase 1 is correct and documented.</done>
</task>

</tasks>

<verification>
Check that all three core planning files (.planning/ROADMAP.md, .planning/STATE.md, .planning/REQUIREMENTS.md) are present, valid markdown, and internally consistent with each other regarding Phase 1.
</verification>

<success_criteria>
1. ROADMAP.md has valid GSD structure.
2. STATE.md accurately tracks Phase 1.
3. REQUIREMENTS.md shows TEST-RM mapped to Phase 1.
</success_criteria>

<output>
After completion, create `.planning/phases/01-roadmap-generation/01-01-SUMMARY.md`
</output>
