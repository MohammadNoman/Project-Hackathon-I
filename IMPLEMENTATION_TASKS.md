# Implementation Tasks - PROJECT_ANALYSIS.md

## Phase 1: Critical Fixes (Priority: CRITICAL ⚠️)

### 1.1 Agent Dispatch Infrastructure
- [ ] Create `reusable-intelligence/` directory
- [ ] Create `reusable-intelligence/dispatch.ps1` script
- [ ] Test dispatch script with dry-run mode
- [ ] Verify agent loading functionality

### 1.2 Path Reference Fixes
- [ ] Update CLAUDE.md path references (reusable-intelligence → .claude)
- [ ] Verify all agent references point to correct locations
- [ ] Test command execution paths

### 1.3 Duplicate Spec Cleanup
- [ ] Delete `specs/1-physical-ai-textbook/`
- [ ] Delete `specs/ai-native-physical-ai-humanoid-robotics-textbook/`
- [ ] Delete `specs/master/`
- [ ] Verify no broken references to deleted specs

## Phase 2: Organization (Priority: MEDIUM 🟡)

### 2.1 Documentation Structure
- [ ] Create `docs/` directory structure
  - [ ] `docs/architecture/`
  - [ ] `docs/features/personalization/`
  - [ ] `docs/features/translation/`
  - [ ] `docs/demo/`
  - [ ] `docs/retrospectives/`
- [ ] Move `DEMO_VIDEO_SCRIPT.md` → `docs/demo/`
- [ ] Move `LESSONS_LEARNED.md` → `docs/retrospectives/`
- [ ] Move personalization docs → `docs/features/personalization/`
- [ ] Move translation docs → `docs/features/translation/`
- [ ] Delete `CLEANUP_PLAN.md`
- [ ] Move `cleanup-structure.ps1` → `history/scripts/`

### 2.2 Skill Directory Population
- [ ] Create skill file for `gemini-delegator/`
- [ ] Create skill file for `visual-excellence/`
- [ ] Create `better-auth-patterns/` skill directory
- [ ] Create skill file for `better-auth-patterns/`

### 2.3 Additional Commands
- [ ] Create `/deploy-frontend` command
- [ ] Create `/deploy-backend` command
- [ ] Create `/setup-env` command
- [ ] Create `/index-content` command

## Phase 3: Enhancement (Priority: LOW 🟢)

### 3.1 Auto-Detection System
- [ ] Create `.claude/commands/auto-delegate.md`
- [ ] Implement keyword detection rules
- [ ] Add execution logic to dispatch.ps1
- [ ] Test auto-delegation with sample tasks

### 3.2 Project Optimization
- [ ] Create `.claudeignore` file
- [ ] Create `docs/README.md` (documentation index)
- [ ] Add OpenAPI configuration to FastAPI
- [ ] Verify all template references in CLAUDE.md

### 3.3 Additional Agents
- [ ] Create `qwen-agent.md`
- [ ] Create `deployment-agent.md`
- [ ] Update CLAUDE.md with new agent documentation

## Verification Tasks
- [ ] Run all tests to ensure nothing broke
- [ ] Verify agent dispatch works end-to-end
- [ ] Test command shortcuts
- [ ] Validate all documentation links
- [ ] Check for any remaining broken references
