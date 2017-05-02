/*
 * This file is part of the PSL software.
 * Copyright 2011-2015 University of Maryland
 * Copyright 2013-2015 The Regents of the University of California
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package edu.umd.cs.psl.util.datasplitter.splitstep;

import java.util.Collection;
import java.util.List;
import java.util.Random;

import edu.umd.cs.psl.database.Database;
import edu.umd.cs.psl.database.Partition;

/**
 * 
 * @author Bert Huang bert@cs.umd.edu
 *
 */
public interface SplitStep {

	List<Collection<Partition>> getSplits(Database inputDB, Random random);
	
}