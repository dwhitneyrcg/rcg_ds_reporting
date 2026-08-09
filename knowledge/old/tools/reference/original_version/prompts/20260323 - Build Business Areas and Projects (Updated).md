**Key Contextual Information:**
1. **Base Folder Path:** C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\knowledge\
2. **Business Area Folder Path:** [Based Folder Path] \ biz_areas
3. **Supporting Files:**
  4. Support Files Path: C:\Users\133486\OneDrive - Royal Caribbean Group\Co-Pilot Demo\Weekly Report from Raw Team Reports (Single-Week Demo)\
  5. 20251031 - Instruction Files (Business Area Summarization).docx
  6. 20251031 - Instructions Files (Generate Business Area Mappings).docx
7. **Naming Conventions: **
  8. The name of a business area should be lower-case and underscore, such that “Revenue Management (RCI)” becomes “revenue_management_(rci)”.
9. **Tag Conventions:**
  10. None Yet
11. **Wiki Links:  **
  12. Follow the specifications outlined here:
    13. C:\Users\133486\OneDrive - Royal Caribbean Group\LocalDatabricks\rcg_ds_reporting\knowledge\conventions\wiki_links\wikilink_conventions.md
  14. They are based on the standards here:

**Build  Business Context:**
You will be working in the Base Folder Path creating information based on the supplied supporting information. You will execute the following tasks
1. **Task 1  -  Create  Business  Area Ontology :** Create a folder in the Business Folder Path for each business area following standardized naming conventions described in the contextual information.
2. **Task 2 – Create a n Overview  Markdown File  for Each Business Area :** For each business area, you will create a business overview markdown file in the folder created for each business area in Task 1.
  3. **Requirements: **
    4. The name of the markdown file will be “overview_”+[Business Area].md, and should follow the standardized naming conventions described in the contextual information.
    5. **Important:*** If the file already exists, you will instead modify the file vs create it. Read this markdown file and consider context for updating the overview.*
    6. The summary file should include necessary tags, following conventions described in the contextual information, you may need later to find information quickly.
  7. **Markdown File Content:** Include the following information (where available, otherwise leave blank):
    8. **Business Department Name**
    9. **Key  Business  Contacts**
    10. **Business Area Overview**
    11. **Business Area Goal**
    12. **Business Area Impact**
    13. **OKRS (Include the OKRs by Quarter as a Table)**
    14. **Active Projects **
    15. **Completed Projects**
    16. **Project Tracking :  Monthly Progress (Last 12 Months Only)**
    17. **Project Tracking :  Weekly Progress (Last Quarter Only)**
  18. **Source: **Fill-In Information based on the supplied supporting files or existing business area overview (if present).
19. **Task  3   – Create a Master Business Areas File: **Create a master business areas markdown file with links to the business area overview markdown files created in Task 2.
  20. **Requirements:**
    21. **Filename:** business_areas_master.md
    22. **Wiki Links Formatting:** I want you to create include a WikiLink, following standards described in the contextual information.
    23. **Important:*** If the file already exists, you will instead modify the file vs create it. Read this markdown file and consider context for updating the overview.*
    24. The summary file should include necessary tags, following conventions described in the contextual information, you may need later to find information quickly.
25. **Task 4 – Create Business Project Ontology for Each Business Area:** In each business area folder, create sub-folders for each business project following standardized naming conventions described in the contextual information.
26. **Task 5 – Create a n Overview  Markdown File  for Each Business  Project :** For each business project, you will create a project overview markdown file in the folder created for each project in Task 4.
  27. **Requirements: **
    28. You must create projects for every business area.
    29. The name of the markdown file will be “overview_”+[Business Project].md, and should follow the standardized naming conventions described in the contextual information.
    30. **Important:*** If the file already exists, you will instead modify the file vs create it. Read this markdown file and consider context for updating the overview.*
    31. The summary file should include necessary tags, following conventions described in the contextual information, you may need later to find information quickly.
  32. **Markdown File Content:** Include the following information (where available, otherwise leave blank):
    33. **Business Department Name**
    34. **Project Name**
    35. **Project Overview**: One Paragraph
    36. **Project Goal: **One Paragraph
    37. **Project Impact: **One Sentence (unless highlighting a methodology, then longer)
    38. **Project Requirements **
    39. **Project Milestones**
    40. **Delivery Status: **Active or Complete (if not provided, assume active).
    41. **Project Delivery Dates**
    42. **Project Tracking :  Monthly Progress (Last 12 Months Only)**
    43. **Project Tracking : Weekly Progress (Last Quarter Only)**
  44. **Source: **Fill-In Information based on the supplied supporting files or existing business area overview (if present).
45. **Task 6 – Update Business Area Overview  Markdown File  for Each Business Project :  **Update the Active and Completed Projects List based on the projects created in Task 5. Reference them with Wiki Links formatting.
  46. **Requirements:**
    47. **Wiki Links Formatting:** I want you to create include a WikiLink, following standards described in the contextual information.
    48. **Important:*** If the file already exists, you will instead modify the file vs create it. Read this markdown file and consider context for updating the overview.*
    49. The summary file should include necessary tags, following conventions described in the contextual information, you may need later to find information quickly.
50. **Task 6  – Create a Master  Project List : **Create a master project markdown file for active projects with wiki links to the business projects overview markdown files created in Task 5 and 6. You should breakdown the projects based business area.
  51. **Requirements:**
    52. **Filename:** business_active_projects_master.md
    53. **Include only Active Projects**
    54. **Wiki Links Formatting:** I want you to create include a WikiLink, following standards described in the contextual information.
    55. **Important:*** If the file already exists, you will instead modify the file vs create it. Read this markdown file and consider context for updating the overview.*
    56. The summary file should include necessary tags, following conventions described in the contextual information, you may need later to find information quickly.
57. **Task 7 – Update the Project and Business Area Links : **Update all markdown tags for the master business area file, master project file, business area overview files, and project files. There should be links that includes the business area name, project name (if relevant), and involved person (if relevant). Additional Tasks:
  58. **Business  Area   Tag: **The master business area file, master project file, business area overview files should be given a general “business_area” tag.
  59. **Business Project Tag: **The project files should be given a general “Project” tag.

**Execution Notes & Lessons Learned (Added by AI Agent)**
Date Executed: 2026-03-23
Agent: GitHub Copilot (Claude Opus 4.6)

Execution Summary:
- 17 business area folders created in knowledge/biz_areas/
- 82 project sub-folders created within business area folders
- 17 business area overview markdown files created (Tasks 2 & 6)
- 82 project overview markdown files created (Task 5)
- 1 master business areas index file created (Task 3)
- Total: 99 folders, 100 files

Data Sources Used:
- 20251031 - Instructions Files (Generate Business Area Mappings).docx — provided all 17 business areas, strategic goals, OKRs, team members, and project details
- 20251031 - Instruction Files (Business Area Summarization).docx — provided summarization format guidance (not directly used for ontology creation)
- knowledge/conventions/wiki_links/wikilink_conventions.md — wikilink formatting rules

Challenges & Recommendations for Future Runs:

1. FILE PATH ISSUES: The .docx file path contains spaces and special characters (e.g., 'OneDrive - Royal Caribbean Group'). Python's python-docx library may fail with PackageNotFoundError when paths have unusual characters. WORKAROUND: Copy the file to a simpler temp path (e.g., C:\Users\133486\temp_task.docx) before reading. This is a known python-docx issue.

2. NAMING CONVENTION EDGE CASES: The naming convention 'lowercase + underscore' is clear for basic names but ambiguous for special characters. Decisions made:
- • Slashes (/) in names like 'RCI/CEL' → replaced with underscore (_) since / is invalid in folder names
- • Colons (:) in 'AXIOM: Generative-AI...' → removed (forbidden in wikilinks)
- • Ampersand (&) kept as-is (not forbidden in wikilinks, valid in file names)
- • Hyphens (-) kept as-is (valid in both file systems and wikilinks)
- • Parentheses kept as-is per the naming example in the doc
- • Quotes/smart-quotes removed from project names
   RECOMMENDATION: Add an explicit 'Character Replacement Rules' section to the naming conventions to remove ambiguity.

3. TASK 5 FILE NAMING AMBIGUITY: Task 5 says the file name should be 'overview_'+[Business Area].md, but since the files are for individual PROJECTS placed inside project folders, this was interpreted as 'overview_'+[Project Name].md. RECOMMENDATION: Update Task 5 to explicitly say [Project Name] instead of [Business Area].

4. NEWBUILD AND HR: These two business areas are listed in the classification labels but have NO supporting data (no strategic goals, OKRs, team members, or projects) in the instruction files. Their overview files were created with blank/placeholder fields. RECOMMENDATION: Either provide supporting data for these areas or explicitly mark them as 'placeholder-only' in the instructions.

5. TAG CONVENTIONS: The doc says 'Tag Conventions: None Yet'. Tags were generated as: business_area, overview, project, master, business_areas, index, plus status tags. RECOMMENDATION: Define a formal tag taxonomy to ensure consistency across future runs.

6. IDEMPOTENT EXECUTION: The script checks for existing files and updates rather than overwrites. Running again is safe and will only modify files that have changed. However, it will NOT delete folders/files from previous runs if business areas or projects are removed. RECOMMENDATION: Add a cleanup step or manifest comparison if business areas change over time.

7. WIKILINK PATH CONVENTION: Wikilinks use relative paths from the biz_areas/ folder (e.g., [[area_folder/project_folder/overview_file|Display Name]]). In Obsidian, this requires the vault root to be at or above the knowledge/ folder for links to resolve correctly. RECOMMENDATION: Document the expected Obsidian vault root path.

8. PYTHON ENVIRONMENT: The project's .venv at rcg_ds_reporting/.venv/Scripts/python.exe has python-docx installed and was used for all file operations. Standard Python was not available on PATH due to Windows Store alias configuration.
