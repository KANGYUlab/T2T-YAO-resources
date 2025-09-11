<h1 align="center">T2T-YAO resources</h1>
<p align="center"><em>Telomere‑to‑telomere diploid human assembly of individual YAO</em></p>
<p align="center">
  <a href="./LICENSE"><img alt="License: CC0-1.0" src="https://img.shields.io/badge/License-CC0%201.0-blue.svg"></a>
  &nbsp;•&nbsp;
  <a href="https://ngdc.cncb.ac.cn/gsa-human/browse/HRA011075">Data v2.0 (HRA011075)</a>
  &nbsp;•&nbsp;
  <a href="https://ngdc.cncb.ac.cn/gsa-human/browse/HRA004987">Data v1.1 (HRA004987)</a>
</p>

<br/>

T2T‑YAO is a telomere‑to‑telomere diploid human assembly for the individual YAO, providing fully phased maternal (mat) and paternal (pat) haplotypes. The v2.0 release integrates ONT ultra‑long, PacBio Revio/HiFi, Element AVITI and Pore‑C sequencing, and distributes aligned BAMs for downstream benchmarking; v1.1 is the initial public release. Assembly evaluation leverages the SAS (Sufficient Alignment Support) framework to profile base‑level and structural errors across technologies ([SAS pipeline](https://github.com/KANGYUlab/sas-pipeline)). For additional background and methodology, see the T2T‑YAO preprint on bioRxiv ([link](https://www.biorxiv.org/content/10.1101/2025.08.01.667781v1.full)).

<hr/>

### T2T-YAO v2.0

- **Genome assemblies**
  - maternal haplotype (mat): [FASTA](https://download.cncb.ac.cn/gwh/Animals/Homo_sapiens_T2T_YAO_v2_mat_GWHGEYC00000000.1/GWHGEYC00000000.1.genome.fasta.gz)
  - paternal haplotype (pat): [FASTA](https://download.cncb.ac.cn/gwh/Animals/Homo_sapiens_T2T_YAO_v2_pat_GWHGEYB00000000.1/GWHGEYB00000000.1.genome.fasta.gz)

- **Raw sequencing data**: [NGDC HRA011075](https://ngdc.cncb.ac.cn/gsa-human/browse/HRA011075)

- **Raw sequencing data details**

  <table>
    <thead>
      <tr>
        <th>Group</th>
        <th>Library</th>
        <th>Platform</th>
        <th>URL</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>YAO_dipo</td>
        <td>ONT</td>
        <td>OXFORD_NANOPORE PromethION</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA011075/HRR2321878/HRR2321878.fq.gz">download</a></td>
      </tr>
      <tr>
        <td>YAO_dipo</td>
        <td>Pore-C</td>
        <td>OXFORD_NANOPORE PromethION</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA011075/HRR2321879/HRR2321879.fastq.gz">download</a></td>
      </tr>
      <tr>
        <td>YAO_dipo</td>
        <td>Revio</td>
        <td>PacBio Revio</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA011075/HRR2321880/HRR2321880.fastq.gz">download</a></td>
      </tr>
      <tr>
        <td rowspan="2">YAO_dipo</td>
        <td rowspan="2">Element</td>
        <td rowspan="2">Element AVITI</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA011075/HRR2321881/HRR2321881_f1.fq.gz">download</a></td>
      </tr>
      <tr>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA011075/HRR2321881/HRR2321881_r2.fq.gz">download</a></td>
      </tr>
      <tr>
        <td>YAO_dipo</td>
        <td>SPRQ</td>
        <td>PacBio Revio</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA011075/HRR2690401/HRR2690401.fq.gz">download</a></td>
      </tr>
    </tbody>
  </table>

- **BAM alignment files**

  | Group | Library | URL |
  | --- | --- | --- |
  | YAO_dipo | ONT | [download](https://download.cncb.ac.cn/gsa-human/HRA011075/HRR2695327/HRR2695327.bam) |
  | YAO_dipo | SPRQ | [download](https://download.cncb.ac.cn/gsa-human/HRA011075/HRR2695328/HRR2695328.bam) |
  | YAO_dipo | Element | [download](https://download.cncb.ac.cn/gsa-human/HRA011075/HRR2695329/HRR2695329.bam) |

- **Gene annotation files**

  | File | Description | URL |
  | --- | --- | --- |
  | yao-v2.0.mat.gff.gz | Gene annotation for maternal haplotype (GFF3, compressed) | [download](https://github.com/KANGYUlab/T2T-YAO-resources/raw/main/yao-v2.0.mat.gff.gz) |
  | yao-v2.0.pat.gff.gz | Gene annotation for paternal haplotype (GFF3, compressed) | [download](https://github.com/KANGYUlab/T2T-YAO-resources/raw/main/yao-v2.0.pat.gff.gz) |


  The annotation covers all 22 autosomes and the X/Y chromosome for both haplotypes, providing comprehensive gene models for downstream analysis and comparison.



<hr/>

### T2T-YAO v1.1

- **Genome assemblies**
  - maternal haplotype (mat): [FASTA](https://download.cncb.ac.cn/gwh/Animals/Homo_sapiens_v1.1_GWHDQZJ00000000/GWHDQZJ00000000.genome.fasta.gz)
  - paternal haplotype (pat): [FASTA](https://download.cncb.ac.cn/gwh/Animals/Homo_sapiens_ChTY001.v1.1_pat_GWHDOOG00000000/GWHDOOG00000000.genome.fasta.gz)

- **Raw sequencing data**: [NGDC HRA004987](https://ngdc.cncb.ac.cn/gsa-human/browse/HRA004987)

- **Raw sequencing data details**

  <table>
    <thead>
      <tr>
        <th>Group</th>
        <th>Library</th>
        <th>Platform</th>
        <th>URL</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>YAO_dipo</td>
        <td>ONT</td>
        <td>OXFORD_NANOPORE PromethION</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA004987/HRR1274612/HRR1274612.fq.gz">download</a></td>
      </tr>
      <tr>
        <td>YAO_dipo</td>
        <td>Hifi</td>
        <td>Pacbio Sequel II</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA004987/HRR1274613/HRR1274613.fastq.gz">download</a></td>
      </tr>
      <tr>
        <td rowspan="2">YAO_dipo</td>
        <td rowspan="2">NGS</td>
        <td rowspan="2">DNBSEQ-T7</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA004987/HRR1274614/HRR1274614_f1.fq.gz">download</a></td>
      </tr>
      <tr>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA004987/HRR1274614/HRR1274614_r2.fq.gz">download</a></td>
      </tr>
      <tr>
        <td>YAO_dipo</td>
        <td>Bionano</td>
        <td>BioNano SAPHYR</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA004987/HRR1274615/HRR1274615.bnx.gz">download</a></td>
      </tr>
      <tr>
        <td rowspan="2">YAO_pat</td>
        <td rowspan="2">NGS</td>
        <td rowspan="2">DNBSEQ-T7</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA004987/HRR1274616/HRR1274616_f1.fq.gz">download</a></td>
      </tr>
      <tr>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA004987/HRR1274616/HRR1274616_r2.fq.gz">download</a></td>
      </tr>
      <tr>
        <td rowspan="2">YAO_mat</td>
        <td rowspan="2">NGS</td>
        <td rowspan="2">DNBSEQ-T7</td>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA004987/HRR1274617/HRR1274617_f1.fq.gz">download</a></td>
      </tr>
      <tr>
        <td><a href="https://download.cncb.ac.cn/gsa-human/HRA004987/HRR1274617/HRR1274617_r2.fq.gz">download</a></td>
      </tr>
    </tbody>
  </table>

---

### Issues

Known issues are tracked in GitHub issues. If you find any errors in the latest version, please raise an issue. Your feedback will help us build more perfect genomic resources.

### License

All data is released to the public domain (CC0 1.0). See [LICENSE](./LICENSE).

### Citation

If you use T2T‑YAO resources, please cite the following references:

1. He, Y., Chu, Y., Guo, S., Hu, J., Li, R., Zheng, Y., Ma, X., Du, Z., Zhao, L., Yu, W., et al. (2023). T2T‑YAO: A Telomere‑to‑telomere Assembled Diploid Reference Genome for Han Chinese. Genomics, Proteomics & Bioinformatics. doi: https://doi.org/10.1016/j.gpb.2023.08.001
2. Yanan Chu, Zhuo Huang, Changjun Shao, Shuming Guo, Xinyao Yu, Jian Wang, Yabin Tian, Jing Chen, Ran Li, Yukun He, Jun Yu, Jie Huang, Zhancheng Gao, Yu Kang.  Approaching an Error-Free Diploid Human Genome. bioRxiv 2025.08.01.667781; doi: https://doi.org/10.1101/2025.08.01.667781

### Changelog

- 2025-08: T2T-YAO v2.0 release
- 2023-08: T2T-YAO v1.1 release

