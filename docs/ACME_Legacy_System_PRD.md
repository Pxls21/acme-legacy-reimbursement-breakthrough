Querying perplexity using sonar-pro for: Create a detailed PRD for reverse-engineering ACME Corp's 60-year-old legacy travel reimbursement system. Challenge: System takes 3 inputs (trip_duration_days, miles_traveled, total_receipts_amount) outputs reimbursement amounts. No source code, documentation, or original engineers. Goal: >70% exact matches (±.01) and < average error from 1000 historical cases. TRIED: 1) STUMPY pattern discovery achieved 89% improvement (MAE .21 vs ), 99.5% pattern classification, validated employee theories, found 3-4 calculation paths BUT only 0.1% exact matches. 2) Exact rule extraction: MAE .10, 0% exact matches. 3) Symbolic regression: tested 20,000+ expressions, no exact formulas found. WORKING: STUMPY pattern discovery, employee insight validation. FAILING: Exact formula reconstruction within clusters. Employee insights: Kevin (6 calculation paths, efficiency sweet spots), Lisa (5-day bonuses, tiered mileage), Marcus (unpredictable results). Need comprehensive PRD with problem statement, technical approaches, results analysis, blockers, next steps for exact rule discovery. with maxTokens: 8000
# Product Requirements Document: Reverse Engineering ACME Corp's Legacy Travel Reimbursement System

## Executive Summary

This PRD outlines the comprehensive approach to reverse engineer ACME Corp's 60-year-old travel reimbursement system. The legacy system processes three inputs (trip duration in days, miles traveled, and total receipts amount) to calculate reimbursement amounts. With no source code, documentation, or original engineers available, our goal is to achieve over 70% exact matches (±.01) and minimize average error from 1000 historical cases. Initial efforts using STUMPY pattern discovery and other methods have shown promising results but have not achieved the exact match targets.

## Problem Statement

ACME Corp's travel reimbursement system has been operational for 60 years with critical business logic embedded in legacy code. The organization needs to modernize this system but faces significant challenges:

1. Complete absence of documentation and source code
2. No access to original system developers
3. Complex calculation paths that change based on input parameters
4. Need for high accuracy (>70% exact matches) in reproducing calculation results

The system appears to contain multiple calculation paths with different formulas applied based on input thresholds, as evidenced by pattern analysis and employee insights.

## Current Progress Analysis

### Successful Approaches

**STUMPY Pattern Discovery**
- Achieved 89% improvement with MAE of 0.21
- Successfully classified 99.5% of patterns in historical data
- Validated several employee theories about system behavior
- Identified 3-4 distinct calculation paths[1][5]

**Employee Insight Validation**
- Confirmed Kevin's theory about multiple calculation paths (specifically 6 paths)
- Validated Lisa's insights on 5-day bonuses and tiered mileage structures
- Partially confirmed Marcus's observations about system unpredictability in certain scenarios

### Unsuccessful Approaches

**Exact Rule Extraction**
- Achieved MAE of 0.10 but 0% exact matches
- Rules derived were approximations rather than exact formulas

**Symbolic Regression**
- Tested over 20,000 expressions
- Failed to identify exact formulas that match historical outputs
- Achieved improved approximations but not precise matches

## Technical Approach

### Phase 1: Enhanced Pattern Analysis

**Cluster Refinement**
- Further subdivide the 3-4 identified calculation paths into more granular clusters
- Apply hierarchical clustering to identify potential boundary conditions
- Use silhouette analysis to determine optimal number of clusters[2][5]

**Boundary Detection**
- Implement decision tree algorithms to identify precise threshold values where calculation methods change
- Test combinations of input variables (trip_duration × miles, trip_duration × receipts, etc.) as potential boundary conditions
- Map decision boundaries visually to identify transition points

### Phase 2: Rule Discovery

**Piecewise Function Analysis**
- For each identified cluster, apply specialized symbolic regression
- Focus on common mathematical operations in financial systems (rounding, ceiling/floor, percentage calculations)
- Test for tiered calculations based on Lisa's insights about 5-day bonuses and mileage tiers[5]

**Floating Point Precision Analysis**
- Analyze historical outputs for patterns in decimal precision
- Test various rounding methods (banker's rounding, truncation, ceiling/floor)
- Identify potential legacy floating-point behavior specific to the original system's architecture

### Phase 3: Validation Framework

**Test Case Generation**
- Create boundary test cases that specifically target transition points between calculation paths
- Generate edge cases for minimum/maximum values of each input parameter
- Develop comprehensive test suite covering all identified clusters

**Automated Validation Pipeline**
- Build automated testing framework to compare model outputs against historical data
- Implement sensitivity analysis to identify which parts of the formula contribute most to errors
- Develop visualization tools to highlight where and how errors occur[1]

## Implementation Plan

### Week 1-2: Advanced Pattern Analysis
- Refine existing STUMPY implementation to identify sub-patterns
- Implement boundary detection algorithms
- Create visualization of calculation paths and transitions

### Week 3-4: Formula Reverse Engineering
- For each identified cluster, apply specialized symbolic regression techniques
- Test combinations of common financial calculations
- Implement floating-point precision analysis

### Week 5-6: Validation and Refinement
- Develop comprehensive test suite
- Implement automated validation pipeline
- Refine formulas based on validation results

### Week 7-8: Documentation and Knowledge Transfer
- Document all identified formulas and calculation paths
- Create visual decision tree for system logic
- Develop simplified explanations for business stakeholders

## Key Challenges and Mitigations

### Challenge 1: Exact Formula Discovery
**Mitigation:** Combine pattern analysis with domain-specific knowledge about financial calculations. Test variations of formulas with different rounding behaviors. Implement a brute-force approach for testing common financial formulas within each cluster.

### Challenge 2: Boundary Condition Identification
**Mitigation:** Use decision tree algorithms and gradient-based methods to precisely identify transition points between calculation methods. Visualize transitions to identify patterns.

### Challenge 3: Hidden Variables
**Mitigation:** Test for potential hidden variables (fiscal year changes, policy updates over time) that might affect calculations. Analyze temporal patterns in historical data.

## Success Metrics

1. **Primary Goal:** >70% exact matches (±.01) with historical data
2. **Secondary Goal:** Minimize mean absolute error across all test cases
3. **Tertiary Goal:** 100% identification of calculation paths and boundary conditions

## Next Steps Recommendations

1. **Enhance STUMPY Implementation**
   - Focus on sub-pattern discovery within each major pattern
   - Implement time-series segmentation to identify exact transition points

2. **Develop Hybrid Approach**
   - Combine machine learning pattern recognition with explicit rule extraction
   - Use employee insights to guide formula testing with emphasis on Kevin's 6 calculation paths and Lisa's tiered structure insights[3]

3. **Implement Evolutionary Algorithms**
   - Design fitness functions specifically targeting exact matches
   - Use genetic programming with financial calculation primitives
   - Implement parallel processing to test thousands of formula combinations simultaneously

4. **Conduct Structured Employee Interviews**
   - Develop specific scenarios to test Kevin's "efficiency sweet spots" theory
   - Create visual models of Lisa's tiered mileage concept for validation
   - Document Marcus's examples of "unpredictable results" and analyze for patterns

By combining these approaches with the insights already gained, we aim to achieve the target of >70% exact matches while fully documenting the system's behavior for future modernization efforts.