---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files must strictly follow the template structure defined in [`templates/assignment-template.md`](../../templates/assignment-template.md). Consistency across all assignments ensures a professional, student-friendly learning experience.

## 1. Required File and Structure

- **File name**: Must be `README.md` in each assignment folder
- **Structure**: Follow the template exactly—do not create custom sections or modify required sections
- **Icons**: Use the exact emoji icons specified in the template for visual consistency
  - 📘 for the assignment title
  - 🎯 for the Objective section
  - 📝 for the Tasks section
  - 🛠️ for individual task titles

## 2. Section Requirements

### Title
- Format: `# 📘 Assignment: [Assignment Title]`
- Use a clear, concise name (e.g., `Python Basics`, `Classes and Objects`, `Data Analysis`)

### Objective (🎯)
- Write 1-2 sentences describing what students will learn or accomplish
- Focus on skills and learning outcomes
- Be specific and measurable
- Example: "Practice fundamental Python programming skills including user input, string formatting, arithmetic operations, and conditional statements by implementing simple functions."

### Tasks (📝)
Each task must include:
- **Task Header**: Format as `### 🛠️ [Task Title]` with specific, action-oriented names
- **Description**: Clearly explain what the student must do (1-2 sentences)
- **Requirements**: Bullet-pointed list of expected outcomes/features that are measurable and specific
- **Examples**: Include code blocks with example input/output when helpful

## 3. Formatting Standards

- Do not add extra sections beyond Title, Objective, and Tasks
- Use markdown code blocks with language specification for code examples:
  ```python
  # Example code here
  ```
- Keep language student-friendly and encouraging
- Maintain consistent indentation and spacing

## 4. Review Checklist

Before submitting an assignment README:
- [ ] File is named `README.md`
- [ ] Title uses 📘 icon
- [ ] Objective section uses 🎯 icon  
- [ ] Tasks section uses 📝 icon
- [ ] Each task uses 🛠️ icon
- [ ] All required sections present (no custom sections added)
- [ ] Requirements are specific and measurable
- [ ] Code examples use proper markdown formatting